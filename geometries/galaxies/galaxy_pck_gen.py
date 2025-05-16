import json
import math as m
import os
from pathlib import Path
import subprocess

def hms2deg(hms_set):
    """Convert hh:mm:ss.ss format of RA to decimal degrees (open source code).

    Args:
        hms_set (set): RA set in sexigesimal coordinates from .JSON list of galaxies

    Returns:
        float: RA in decimal degrees
    """

    # Convert .JSON set into string and split into time units based on colon placement
    hms_str = next(iter(hms_set))
    hours, minutes, seconds = map(float, hms_str.split(':'))
    degrees = (hours + minutes / 60 + seconds / 3600) * 15

    return degrees

def dms2deg(dms_set):
    """Convert dd\u00b0mm'ss.ss" format of DEC to decimal degrees (open source code).

    Args:
        dms_set (set): DEC set in sexigesimal coordinates from .JSON list of galaxies

    Returns:
        float: DEC in decimal degrees
    """

    # Convert .JSON set into string
    dms_str = next(iter(dms_set))

    # Remove degree, minute, second symbols and split
    dms_str = dms_str.replace("\u00b0", " ").replace("'", " ").replace("\"", "")
    parts = dms_str.strip().split()

    # Extract sign
    sign = -1 if parts[0].startswith("-") else 1

    # Absolute value parsing
    degrees = abs(float(parts[0]))
    minutes = float(parts[1])
    seconds = float(parts[2])

    # Convert to decimal degrees
    decimal_deg = sign * (degrees + minutes / 60 + seconds / 3600)

    return decimal_deg

def main():
    """Creates and/or updates PCK files for each galaxy in a .JSON list.

    Args:
        None

    Returns:
        None
    """
    # Load galaxy data
    cwd = Path.cwd()
    json_rel_path = 'geometries/galaxies/galaxies.json'
    tpc_rel_path = 'geometries/galaxies/'
    json_filename = os.path.join(cwd, json_rel_path)

    # Load .JSON file
    with open(json_filename, "r") as f:
        galaxies = json.load(f)

    # Track the next available ID
    used_ids = {g["id"] for g in galaxies if g["id"]}
    next_id = 9999000

    while str(next_id) in used_ids:
        next_id += 1

    # Update IDs and create .tpc files
    for galaxy in galaxies:

        # Assign new ID if missing
        if not galaxy["id"]:
            galaxy["id"] = str(next_id)
            next_id += 1

        # Write PCK
        tpc_filename = os.path.join(tpc_rel_path, f"{galaxy['name'].replace(' ', '_')}.tpc")

        with open(tpc_filename, "w") as tpc_file:

            tpc_file.write(f"\\begindata\n")
            tpc_file.write(f"NAIF_BODY_NAME        += ( \'{galaxy['name']}\' )\n")
            tpc_file.write(f"NAIF_BODY_CODE        += ( {galaxy['id']} )\n")
            tpc_file.write(f"NH_TARGET_BODIES      += ( {galaxy['id']} )\n")

            # Convert RA/DEC values from .JSON into decimal degree units
            ra_deg = hms2deg({galaxy['RA']})
            dec_deg = dms2deg({galaxy['DEC']})

            tpc_file.write(f"BODY{galaxy['id']}_POLE_RA    = (" + str(ra_deg) + " 0. 0.)\n")
            tpc_file.write(f"BODY{galaxy['id']}_POLE_DEC   = (" + str(dec_deg) + " 0. 0.)\n")


            tpc_file.write(f"BODY{galaxy['id']}_PM         = (0. 0. 0.)\n")
            tpc_file.write(f"BODY{galaxy['id']}_POLE_RADII = (0. 0. 0.)\n")

            tpc_file.write(f"\\begintext\n\nPINPOINT parameters for galaxy {galaxy['name']}:\n\\begindata\n")

            tpc_file.write(f"SITES                 += ( \'SITE{galaxy['id']}\' )\n")
            tpc_file.write(f"SITE{galaxy['id']}_FRAME      = \'J2000\'\n")
            tpc_file.write(f"SITE{galaxy['id']}_IDCODE     = {galaxy['id']}\n")

            # Use decimal degree RA/DEC values to compute unit vector
            x = str(m.cos(m.radians(ra_deg)) * m.cos(m.radians(dec_deg)))
            y = str(m.sin(m.radians(ra_deg)) * m.cos(m.radians(dec_deg)))
            z = str(m.sin(m.radians(dec_deg)))

            tpc_file.write(f"SITE{galaxy['id']}_XYZ        = (" + x + " " + y + " " + z + ")\n")
            tpc_file.write(f"SITE{galaxy['id']}_CENTER     = -1999\n\\begintext\n")


    # Save updated .JSON
    with open(json_filename, "w") as f:
        json.dump(galaxies, f, indent=4)

    # Confirm code ran successfully
    print("Galaxy IDs updated and .tpc files created.")

    # # # # # # # # # # # # # # # # DRAFT # # # # # # # # # # # # # # # #

    # PINPOINT
    # command = "ls -l"  # list files
    # exit_code = os.system(command)
    # print(f"Exit code: {exit_code}")

    # pinpoint_path = 'geometries/galaxies/pinpoint.exe'
    # pinpoint_filename = os.path.join(cwd, pinpoint_path)

    # pck_path = 'geometries/galaxies/NGC_625.tpc'
    # pck_filename = os.path.join(cwd, pck_path)

    # spk_path = 'geometries/galaxies/NGC_625.bsp'
    # spk_filename = os.path.join(cwd, spk_path)

    # subprocess.run([pinpoint_filename, pck_filename, spk_filename])

    # PS C:\Users\ewolc> [path to pinpoint]
    # Landmark definitions: [path to each PCK]
    # SPK file to make    : [path to each new SPK that should not exist yet]

    # # # # # # # # # # # # # # # # DRAFT # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    main()
