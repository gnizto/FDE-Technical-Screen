def sort(width: float, height: float, length: float, mass: float) -> str:
    is_bulky = _is_bulky(width, height, length)
    is_heavy = _is_heavy(mass)

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

def _is_bulky(width: float, height: float, length: float) -> bool:
    BULKY_VOLUME_REF = 1_000_000
    BULKY_SIDE_REF = 150

    is_area_bulky = (width * height * length) >= BULKY_VOLUME_REF
    is_side_bulky = max(width, height, length) >= BULKY_SIDE_REF
    return is_area_bulky or is_side_bulky 

def _is_heavy(mass: float) -> bool:
    HEAVY_REF = 20
    return mass >= HEAVY_REF

if __name__ == "__main__":
    packages = [
        {
            "id": 1,
            "expected": "STANDARD",
            "input": {
                "width": 50,
                "height": 40,
                "length": 30,
                "mass": 10
            }
        },
        {
            "id": 2,
            "expected": "SPECIAL",
            "input": {
                "width": 200,
                "height": 30,
                "length": 20,
                "mass": 10
            }
        },
        {
            "id": 3,
            "expected": "REJECTED",
            "input": {
                "width": 200,
                "height": 200,
                "length": 200,
                "mass": 25
            }
        }
    ]
    
    for package in packages:
        result = sort(
            package['input']["width"], package['input']["height"], 
            package['input']["length"], package['input']["mass"])
        
        sb = []
        sb.append(f"#{package['id']} {package['input']}:")
        sb.append(f"[{package['expected']==result}]")
        sb.append(f"Expected={package['expected']} returned={result}")
        
        print(" ".join(sb))

