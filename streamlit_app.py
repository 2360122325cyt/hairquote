# -*- coding: utf-8 -*-
import streamlit as st
import sys

# ===================== 以下全部是你原来的数据和函数，原封不动 =====================
PAYPAL_RATE = 0.05
ALIBABA_RATE = 0.024

WEIGHT = {
    "bundle": 100,
    "5x5HD closure": 100,
    "2x6HD closure": 100,
    "6x6HD closure": 100,
    "13x4HD frontal": 100,
    "13x6HD frontal": 100,
    "5x5HD closure wig_180密度": 400,
    "6x6HD closure wig_180密度": 400,
    "13x4HD frontal wig_180密度": 400,
    "13x6HD frontal wig_180密度": 400,
    "5x5HD closure wig_250密度": 500,
    "6x6HD closure wig_250密度": 500,
    "13x4HD frontal wig_250密度": 500,
    "13x6HD frontal wig_250密度": 500,
    "5x5HD closure wig_300密度": 600,
    "6x6HD closure wig_300密度": 600,
    "13x4HD frontal wig_300密度": 600,
    "13x6HD frontal wig_300密度": 600,
}

PROD_CATEGORY = ["bundle", "closure", "frontal", "wig"]

BUNDLE_GRADES = [
    "10a",
    "12a blue band",
    "12a red band",
    "13a white band",
    "Thai raw hair",
    "Super double drawn Thai raw hair",
    "13a T1",
    "13a P1 rose band"
]

CLOSURE_GRADES = [
    "10a 5×5HD",
    "10a 2×6HD",
    "10a 6×6HD",
    "12a blue band 5×5HD",
    "Thai raw hair 5×5HD",
    "Thai raw hair 6×6HD",
    "13a white band 5×5HD",
    "13a white band 6×6HD (1-4pcs)",
    "13a white band 6×6HD (over 5pcs vip)"
]

FRONTAL_GRADES = [
    "10a 13×4HD",
    "10a 13×6HD",
    "Thai raw hair 13×6HD",
    "13a white band 13×6HD"
]

WIG_BASE_TYPE = ["closure", "frontal"]
WIG_DENS_LIST = ["180", "250", "300"]

GRADE_BASE_MAP = {
    "10a": "10a",
    "12a blue band": "12a blue band",
    "12a red band": "12a red band",
    "Thai raw hair": "Thai raw hair",
    "Super double drawn Thai raw hair": "Super double drawn Thai raw hair",
    "13a T1": "13a T1",
    "13a P1 rose band": "13a P1 rose band",
    "13a white band": "13a white band",
    "10a 5×5HD": "10a",
    "10a 2×6HD": "10a",
    "10a 6×6HD": "10a",
    "12a blue band 5×5HD": "12a blue band",
    "Thai raw hair 5×5HD": "Thai raw hair",
    "Thai raw hair 6×6HD": "Thai raw hair",
    "13a white band 5×5HD": "13a white band",
    "13a white band 6×6HD (1-4pcs)": "13a white band",
    "13a white band 6×6HD (over 5pcs vip)": "13a white band",
    "10a 13×4HD": "10a",
    "10a 13×6HD": "10a",
    "10a 13×6HD unified price": "10a",
    "10a 13×6HD split price": "10a",
    "Thai raw hair 13×6HD": "Thai raw hair",
    "13a white band 13×6HD": "13a white band",
}

GRADE_ALLOW_WAVE = {
    "10a": ["straight", "body wave", "loose wave", "deep wave"],
    "12a blue band": ["straight", "body wave", "loose wave", "deep wave", "Burmese curly"],
    "12a red band": ["straight", "body wave", "loose wave", "deep wave", "tiny curly"],
    "Thai raw hair": ["straight", "body wave", "loose wave", "deep wave", "Burmese curly"],
    "Super double drawn Thai raw hair": ["straight", "body wave", "loose wave", "deep wave", "Burmese curly"],
    "13a T1": ["straight", "body wave", "loose wave", "deep wave"],
    "13a P1 rose band": ["straight", "loose wave", "body wave", "tiny curly"],
    "13a white band": ["straight", "body wave", "loose wave", "deep wave", "loose curly", "deep curly", "Burmese curly"]
}
CLOSE_FRONT_WAVES = ["straight", "body wave", "loose wave", "deep wave"]

COUNTRY_LIST = ["USA 美国", "SouthAfrica 南非", "英国"]
PAY_LIST = ["PayPal(5%)", "Alibaba(2.4%)"]
PRICE_TIER_LIST = ["零售价 (Retail)", "VIP价 (VIP)"]

VIP_ENABLED_GRADES = ["13a white band", "12a blue band", "12a red band", "13a T1", "13a P1 rose band"]

SHIP_DATA = {
 "USA 美国": [
        {"min_w":0,"max_w":400,"reg":38.0,"low":26.1},
        {"min_w":400,"max_w":800,"reg":43.4,"low":33.4},
        {"min_w":800,"max_w":1200,"reg":56.4,"low":43.4},
        {"min_w":1200,"max_w":1600,"reg":65.8,"low":50.6},
        {"min_w":1600,"max_w":2100,"reg":78.8,"low":60.6},
        {"min_w":2100,"max_w":2600,"reg":69.6,"low":53.6},
        {"min_w":2600,"max_w":3000,"reg":80.5,"low":61.9},
        {"min_w":3000,"max_w":3400,"reg":87.7,"low":67.5},
        {"min_w":3400,"max_w":3800,"reg":98.6,"low":75.8},
        {"min_w":3800,"max_w":4100,"reg":105.8,"low":81.4},
        {"min_w":4100,"max_w":4400,"reg":112.8,"low":86.7},
        {"min_w":4400,"max_w":4700,"reg":119.9,"low":92.2},
        {"min_w":4700,"max_w":5100,"reg":130.7,"low":100.5},
        {"min_w":5100,"max_w":5400,"reg":137.8,"low":106.0},
        {"min_w":5400,"max_w":5800,"reg":148.6,"low":114.3},
        {"min_w":5800,"max_w":6200,"reg":155.7,"low":119.8},
        {"min_w":6200,"max_w":6600,"reg":166.5,"low":128.1},
        {"min_w":6600,"max_w":7000,"reg":173.7,"low":133.6},
        {"min_w":7000,"max_w":7500,"reg":184.4,"low":141.8},
        {"min_w":7500,"max_w":8000,"reg":191.6,"low":147.4},
        {"min_w":8000,"max_w":8500,"reg":186.3,"low":143.3},
        {"min_w":8500,"max_w":9000,"reg":191.6,"low":147.4},
        {"min_w":9000,"max_w":9500,"reg":200.5,"low":154.2},
        {"min_w":9500,"max_w":10000,"reg":205.8,"low":158.3},
        {"min_w":10000,"max_w":10500,"reg":214.7,"low":165.2},
        {"min_w":10500,"max_w":11000,"reg":220.0,"low":169.2},
        {"min_w":11000,"max_w":11500,"reg":228.9,"low":176.1},
        {"min_w":11500,"max_w":12000,"reg":234.2,"low":180.2},
        {"min_w":12000,"max_w":12500,"reg":243.1,"low":187.0},
        {"min_w":12500,"max_w":13000,"reg":248.4,"low":191.1},
        {"min_w":13000,"max_w":13500,"reg":257.3,"low":197.9},
        {"min_w":13500,"max_w":14000,"reg":262.6,"low":202.0},
        {"min_w":14000,"max_w":14500,"reg":271.5,"low":208.9},
        {"min_w":14500,"max_w":15000,"reg":276.8,"low":212.9},
        {"min_w":15000,"max_w":15500,"reg":285.7,"low":219.8},
        {"min_w":15500,"max_w":16000,"reg":291.0,"low":223.9},
        {"min_w":16000,"max_w":16500,"reg":299.9,"low":230.7},
        {"min_w":16500,"max_w":17000,"reg":305.2,"low":234.8},
        {"min_w":17000,"max_w":17500,"reg":314.1,"low":241.6},
        {"min_w":17500,"max_w":18000,"reg":319.4,"low":245.7},
        {"min_w":18000,"max_w":19000,"reg":328.3,"low":252.6},
        {"min_w":19000,"max_w":20000,"reg":278.4,"low":214.1}
    ],
    "SouthAfrica 南非": [
        {"min_w":0,"max_w":400,"reg":79.07,"low":61.77},
        {"min_w":400,"max_w":800,"reg":68.33,"low":53.38},
        {"min_w":800,"max_w":1200,"reg":85.45,"low":66.76},
        {"min_w":1200,"max_w":1600,"reg":99.07,"low":77.40},
        {"min_w":1600,"max_w":2100,"reg":116.20,"low":90.78},
        {"min_w":2100,"max_w":2600,"reg":127.22,"low":99.39},
        {"min_w":2600,"max_w":3000,"reg":144.50,"low":112.89},
        {"min_w":3400,"max_w":3800,"reg":175.56,"low":137.16},
        {"min_w":3800,"max_w":4100,"reg":189.34,"low":147.92},
        {"min_w":4100,"max_w":4400,"reg":189.44,"low":148.00},
        {"min_w":4400,"max_w":4700,"reg":200.63,"low":156.74},
        {"min_w":4700,"max_w":5100,"reg":215.33,"low":168.23},
        {"min_w":5100,"max_w":5400,"reg":226.52,"low":176.97},
        {"min_w":5400,"max_w":5800,"reg":241.24,"low":None},
        {"min_w":5800,"max_w":6200,"reg":252.43,"low":None},
        {"min_w":6200,"max_w":6600,"reg":267.14,"low":None},
        {"min_w":6600,"max_w":7000,"reg":278.32,"low":None},
        {"min_w":7000,"max_w":7500,"reg":293.04,"low":None},
        {"min_w":7500,"max_w":8000,"reg":304.23,"low":None},
        {"min_w":8000,"max_w":8500,"reg":325.47,"low":None},
        {"min_w":8500,"max_w":9000,"reg":335.21,"low":None},
        {"min_w":9000,"max_w":9500,"reg":348.48,"low":None},
        {"min_w":9500,"max_w":10000,"reg":358.22,"low":None},
        {"min_w":10000,"max_w":10500,"reg":371.49,"low":None}
    ],
    "英国": [
        {"min_w":0,"max_w":400,"reg":50.18,"low":39.19},
        {"min_w":400,"max_w":800,"reg":50.28,"low":39.29},
        {"min_w":800,"max_w":1200,"reg":62.13,"low":48.54},
        {"min_w":1200,"max_w":1600,"reg":72.22,"low":56.42},
        {"min_w":1600,"max_w":2100,"reg":84.07,"low":65.68},
        {"min_w":2100,"max_w":2600,"reg":70.57,"low":55.13},
        {"min_w":2600,"max_w":3000,"reg":80.33,"low":62.76},
        {"min_w":3000,"max_w":3400,"reg":88.33,"low":69.01},
        {"min_w":3400,"max_w":3800,"reg":98.11,"low":76.65},
        {"min_w":3800,"max_w":4100,"reg":106.11,"low":82.9},
        {"min_w":4100,"max_w":4400,"reg":105.88,"low":82.72},
        {"min_w":4400,"max_w":4700,"reg":112.45,"low":87.85},
        {"min_w":4700,"max_w":5100,"reg":120.79,"low":94.37},
        {"min_w":5100,"max_w":5400,"reg":127.37,"low":99.51},
        {"min_w":5400,"max_w":5800,"reg":135.71,"low":106.02},
        {"min_w":5800,"max_w":6200,"reg":142.28,"low":111.16},
        {"min_w":6200,"max_w":6600,"reg":150.63,"low":117.68},
        {"min_w":6600,"max_w":7000,"reg":157.20,"low":122.81},
        {"min_w":7000,"max_w":7500,"reg":165.54,"low":129.33},
        {"min_w":7500,"max_w":8000,"reg":172.11,"low":134.46},
        {"min_w":8000,"max_w":8500,"reg":164.19,"low":128.27},
        {"min_w":8500,"max_w":9000,"reg":169.42,"low":132.36},
        {"min_w":9000,"max_w":9500,"reg":176.41,"low":137.82},
        {"min_w":9500,"max_w":10000,"reg":181.64,"low":141.91},
        {"min_w":10000,"max_w":10500,"reg":188.65,"low":147.38},
        {"min_w":10500,"max_w":11000,"reg":193.88,"low":151.47},
        {"min_w":11000,"max_w":11500,"reg":200.88,"low":156.94},
        {"min_w":11500,"max_w":12000,"reg":206.12,"low":161.03},
        {"min_w":12000,"max_w":12500,"reg":213.12,"low":166.5},
        {"min_w":12500,"max_w":13000,"reg":218.36,"low":170},
        {"min_w":13000,"max_w":13500,"reg":225.36,"low":176.06},
        {"min_w":13500,"max_w":14000,"reg":230.59,"low":180.15},
        {"min_w":14000,"max_w":14500,"reg":237.58,"low":185.61}
    ]
}

PRICE_DB = {
    "bundle": {
        "10a": {
            "straight,body wave,loose wave,deep wave":{
                12:21.50,14:24.70,16:27.20,18:35.50,20:38.30,
                22:41.50,24:48.80,26:53.10,28:55.80,30:60.50
            }
        },
        "12a blue band": {
            "straight,body wave,loose wave": {
                12:25.10,14:28.80,16:31.80,18:39.30,20:51.60,
                22:61.60,24:68.90,26:74.40,28:78.90,30:81.90
            },
            "deep wave": {
                12:26.10,14:29.80,16:32.80,18:40.30,20:52.60,
                22:62.70,24:69.90,26:75.40,28:79.90,30:82.90
            },
            "Burmese curly": {
                12:30.40,14:34.10,16:37.10,18:44.60,20:56.90,
                22:66.90,24:74.10,26:79.70,28:84.20,30:87.10
            }
        },
        "12a red band": {
            "straight,body wave,loose wave,deep wave": {
                12:46.50,14:49.50,16:54.50,18:63.50,20:72.50,
                22:83.00,24:95.30,26:101.10,28:106.50,30:111.50
            },
            "tiny curly": {
                12:47.50,14:50.50,16:55.50,18:64.50,20:73.50,
                22:84.00,24:96.30,26:102.10,28:107.50,30:112.50
            }
        },
        "Thai raw hair": {
            "straight,body wave,loose wave,deep wave,Burmese curly": {
                12:30.00,14:35.70,16:42.70,18:49.60,20:58.30,
                22:65.70,24:81.90,26:89.20,28:93.40,30:104.0
            }
        },
        "Super double drawn Thai raw hair": {
            "straight,body wave,loose wave,deep wave,Burmese curly": {
                12:42.70,14:54.60,16:68.90,18:82.00,20:96.30,
                22:115.40,24:134.40,26:146.30,28:155.80
            }
        },
        "13a T1": {
            "straight,body wave,loose wave,deep wave": {
                12:59.70,14:62.70,16:70.10,18:80.90,20:90.10,
                22:131.50,24:146.70,26:154.00,28:161.20,30:174.00,32:187.00
            }
        },
        "13a P1 rose band": {
            "straight,loose wave,deep wave,tiny curly": {
                12:53.70,14:56.70,16:64.10,18:74.90,20:84.10,
                22:91.50,24:108.10,26:115.30,28:122.50,30:130.00
            },
            "body wave": {
                12:55.50,14:58.50,16:65.90,18:76.70,20:85.90,
                22:93.30,24:109.90,26:117.10,28:124.30,30:131.80
            }
        },
        "13a white band": {
            "straight,loose wave,deep wave": {
                "retail": {
                    10: 32.90, 12: 47.00, 14: 49.70, 16: 56.60, 18: 65.90,
                    20: 74.40, 22: 85.90, 24: 100.00, 26: 106.70, 28: 111.20,
                    30: 120.60, 32: 120.60, 34: 122.70, 36: 125.00
                },
                "vip": {
                    10: 27.90, 12: 42.00, 14: 44.70, 16: 51.60, 18: 60.90,
                    20: 69.40, 22: 80.90, 24: 95.00, 26: 101.70, 28: 106.20,
                    30: 115.60, 32: 115.60, 34: 117.70, 36: 120.00
                }
            },
            "body wave": {
                "retail": {
                    10: 34.20, 12: 48.50, 14: 51.30, 16: 58.10, 18: 67.40,
                    20: 75.90, 22: 87.40, 24: 101.50, 26: 108.30, 28: 112.70,
                    30: 122.10
                },
                "vip": {
                    10: 29.20, 12: 43.50, 14: 46.30, 16: 53.10, 18: 62.40,
                    20: 70.90, 22: 82.40, 24: 96.50, 26: 103.30, 28: 107.70,
                    30: 117.10
                }
            },
            "loose curly,deep curly": {
                "retail": {
                    10: 34.70, 12: 48.90, 14: 51.70, 16: 58.60, 18: 67.90,
                    20: 76.30, 22: 87.90, 24: 102.00, 26: 108.70, 28: 113.10,
                    30: 122.60
                },
                "vip": {
                    10: 29.70, 12: 43.90, 14: 46.70, 16: 53.60, 18: 62.90,
                    20: 71.30, 22: 82.90, 24: 97.00, 26: 103.70, 28: 108.10,
                    30: 117.60
                }
            },
            "Burmese curly": {
                "retail": {
                    12: 58.90, 14: 61.70, 16: 68.60, 18: 77.90,
                    20: 86.30, 22: 97.90, 24: 112.00, 26: 118.70, 28: 123.10,
                    30: 132.60
                },
                "vip": {
                    12: 53.90, 14: 56.70, 16: 63.60, 18: 72.90,
                    20: 81.30, 22: 92.90, 24: 107.00, 26: 113.70, 28: 118.10,
                    30: 127.60
                }
            }
        }
    },
    "closure": {
        "10a 5×5HD": {
            "straight": {12: 26.1, 14: 28.3, 16: 31.7, 18: 35.0, 20: 39.2},
            "body wave,loose wave,deep wave": {12: 27.1, 14: 29.3, 16: 32.7, 18: 36.0, 20: 40.2}
        },
        "10a 2×6HD": {
            "straight,body wave": {12: 38.0, 14: 39.0, 16: 43.0, 18: 47.0, 20: 52.0},
            "loose wave,deep wave": {12: 40.0, 14: 41.0, 16: 45.0, 18: 49.0, 20: 54.0}
        },
        "10a 6×6HD": {
            "straight": {12: 56.30, 14: 60.40, 16: 66.80, 18: 74.40, 20: 84.40},
            "body wave,loose wave,deep wave": {12: 57.50, 14: 61.60, 16: 68.00, 18: 75.60, 20: 85.60}
        },
        "12a blue band 5×5HD": {
            "straight": {12: 40.50, 14: 43.10, 16: 47.50, 18: 52.90, 20: 58.10},
            "body wave,loose wave,deep wave": {12: 42.50, 14: 45.10, 16: 49.50, 18: 54.90, 20: 60.10}
        },
        "Thai raw hair 5×5HD": {
            "straight": {12: 44.4, 14: 46.7, 16: 52.3, 18: 56.6, 20: 61.3},
            "body wave,loose wave,deep wave": {12: 45.4, 14: 47.7, 16: 53.3, 18: 57.6, 20: 62.3}
        },
        "Thai raw hair 6×6HD": {
            "straight": {12: 62.1, 14: 65.5, 16: 72.0, 18: 78.6, 20: 87.4},
            "body wave,loose wave,deep wave": {12: 63.1, 14: 66.5, 16: 73.0, 18: 79.6, 20: 88.4}
        },
        "13a white band 5×5HD": {
            "straight,body wave,loose wave": {12: 97.30, 14: 104.80, 16: 113.30, 18: 121.80, 20: 145.80},
            "deep wave": {12: 105.30, 14: 112.80, 16: 121.30, 18: 129.80, 20: 153.80}
        },
        "13a white band 6×6HD (1-4pcs)": {
            "straight,body wave,loose wave": {12: 107.30, 14: 114.80, 16: 123.30, 18: 131.80, 20: 155.80},
            "deep wave": {12: 115.30, 14: 122.80, 16: 131.30, 18: 139.80, 20: 163.80}
        },
        "13a white band 6×6HD (over 5pcs vip)": {
            "straight,body wave,loose wave": {12: 97.30, 14: 104.80, 16: 113.30, 18: 121.80, 20: 145.80},
            "deep wave": {12: 105.30, 14: 112.80, 16: 121.30, 18: 129.80, 20: 153.80}
        }
    },
    "frontal": {
        "10a 13×4HD": {
            "straight": {12: 45.00, 14: 47.70, 16: 52.10, 18: 57.50, 20: 64.20},
            "body wave,loose wave,deep wave": {12: 46.00, 14: 48.70, 16: 53.10, 18: 58.50, 20: 65.20}
        },
        "10a 13×6HD unified price": {
            "all textures": {12: 137.3, 14: 142.6, 16: 152.4, 18: 166.6, 20: 183.3}
        },
        "10a 13×6HD split price": {
            "straight": {12: 73.00, 14: 78.00, 16: 86.00, 18: 94.00, 20: 107.00},
            "body wave,loose wave,deep wave": {12: 75.00, 14: 80.00, 16: 88.00, 18: 96.00, 20: 109.00}
        },
        "Thai raw hair 13×6HD": {
            "straight": {12: 106.20, 14: 110.30, 16: 120.20, 18: 129.60, 20: 138.70},
            "body wave,loose wave,deep wave": {12: 108.20, 14: 112.30, 16: 122.20, 18: 131.60, 20: 140.70}
        },
        "13a white band 13×6HD": {
            "all textures": {12: 219.10, 14: 249.30, 16: 250.50, 18: 266.60, 20: 289.50, 22: 320.60, 24: 354.70, 26: 397.80, 28: 445.00, 30: 498.30}
        }
    }
}

PRICE_DB["frontal"]["10a 13×6HD"] = PRICE_DB["frontal"]["10a 13×6HD unified price"]

# ===================== 工具函数（完全保留） =====================
def get_ship_fee(total_w, country, ship_key="reg"):
    data = SHIP_DATA.get(country, [])
    for item in data:
        if item["min_w"] < total_w <= item["max_w"]:
            val = item.get(ship_key)
            if val is not None:
                return round(val,2)
    return None

def get_bundle_unit_price(grade, wave, length, tier='retail'):
    grade_data = PRICE_DB["bundle"].get(grade, {})
    for wave_group, len_dict in grade_data.items():
        group_waves = [w.strip() for w in wave_group.split(",")]
        if wave in group_waves:
            if grade == "13a white band":
                tier_dict = len_dict.get(tier, {})
                if length in tier_dict:
                    return tier_dict[length]
                return 0
            else:
                if length in len_dict:
                    retail_price = len_dict[length]
                    if tier == 'vip' and grade in VIP_ENABLED_GRADES:
                        discount = 0
                        if grade == "12a blue band":
                            discount = 5
                        elif grade == "12a red band":
                            discount = 6
                        elif grade == "13a T1":
                            discount = 5
                        elif grade == "13a P1 rose band":
                            discount = 5
                        vip_price = retail_price - discount
                        return vip_price if vip_price > 0 else 0
                    return retail_price
    return 0

def get_base_piece_price(base_type, base_grade, piece_len):
    if base_type == "closure":
        piece_data = PRICE_DB["closure"].get(base_grade, {})
    else:
        piece_data = PRICE_DB["frontal"].get(base_grade, {})
    for wave_group, len_dict in piece_data.items():
        group_waves = [w.strip() for w in wave_group.split(",")]
        if "all textures" in wave_group or "deep wave" in group_waves:
            if piece_len in len_dict:
                return len_dict[piece_len]
    return 0

WIG_CALC_RULE = {
    ("180", 12): {"bundle_len_list": [12,12], "piece_len":12},
    ("180", 14): {"bundle_len_list": [12,14], "piece_len":12},
    ("180", 16): {"bundle_len_list": [14,16], "piece_len":14},
    ("180", 18): {"bundle_len_list": [16,18], "piece_len":16},
    ("180", 20): {"bundle_len_list": [18,20], "piece_len":16},
    ("180", 22): {"bundle_len_list": [20,22], "piece_len":18},
    ("180", 24): {"bundle_len_list": [22,24], "piece_len":18},
    ("180", 26): {"bundle_len_list": [24,26], "piece_len":20},
    ("180", 28): {"bundle_len_list": [26,28], "piece_len":20},
    ("180", 30): {"bundle_len_list": [28,30], "piece_len":20},
    ("250", 12): {"bundle_len_list": [12,12,12], "piece_len":12},
    ("250", 14): {"bundle_len_list": [12,12,14], "piece_len":12},
    ("250", 16): {"bundle_len_list": [12,14,16], "piece_len":14},
    ("250", 18): {"bundle_len_list": [14,16,18], "piece_len":16},
    ("250", 20): {"bundle_len_list": [16,18,20], "piece_len":16},
    ("250", 22): {"bundle_len_list": [18,20,22], "piece_len":18},
    ("250", 24): {"bundle_len_list": [20,22,24], "piece_len":18},
    ("250", 26): {"bundle_len_list": [22,24,26], "piece_len":20},
    ("250", 28): {"bundle_len_list": [24,26,28], "piece_len":20},
    ("250", 30): {"bundle_len_list": [26,28,30], "piece_len":20},
    ("300", 12): {"bundle_len_list": [12,12,12,12], "piece_len":12},
    ("300", 14): {"bundle_len_list": [12,12,12,14], "piece_len":12},
    ("300", 16): {"bundle_len_list": [12,12,14,16], "piece_len":14},
    ("300", 18): {"bundle_len_list": [12,14,16,18], "piece_len":16},
    ("300", 20): {"bundle_len_list": [14,16,18,20], "piece_len":16},
    ("300", 22): {"bundle_len_list": [16,18,20,22], "piece_len":18},
    ("300", 24): {"bundle_len_list": [18,20,22,24], "piece_len":18},
    ("300", 26): {"bundle_len_list": [20,22,24,26], "piece_len":20},
    ("300", 28): {"bundle_len_list": [22,24,26,28], "piece_len":20},
    ("300", 30): {"bundle_len_list": [24,26,28,30], "piece_len":20},
}

def calc_wig_total_cost(bundle_grade, base_type, base_grade, density, wig_len, wave, tier='retail'):
    rule_key = (density, wig_len)
    if rule_key not in WIG_CALC_RULE:
        return 0
    rule = WIG_CALC_RULE[rule_key]
    bundle_len_list = rule["bundle_len_list"]
    piece_use_len = rule["piece_len"]
    sum_bundle = 0
    for l in bundle_len_list:
        price = get_bundle_unit_price(bundle_grade, wave, l, tier)
        if price <= 0:
            return 0
        sum_bundle += price
    piece_cost = get_base_piece_price(base_type, base_grade, piece_use_len)
    if piece_cost <= 0:
        return 0
    total = sum_bundle + piece_cost + 5
    return round(total,2)

def calc_normal_price(prod_cat, grade, wave, length, tier='retail'):
    if prod_cat == "bundle":
        return get_bundle_unit_price(grade, wave, length, tier)
    elif prod_cat in ["closure", "frontal"]:
        cat_data = PRICE_DB[prod_cat].get(grade, {})
        for wave_group, len_dict in cat_data.items():
            group_wave_list = [w.strip() for w in wave_group.split(",")]
            if "all textures" in wave_group:
                if length in len_dict:
                    return len_dict[length]
            if wave in group_wave_list:
                if length in len_dict:
                    return len_dict[length]
        return 0
    return 0

# ===================== Streamlit UI（替换 Tkinter） =====================
def main():
    st.set_page_config(page_title="💇 假发专业报价系统", layout="wide")
    st.title("💇 假发专业报价系统 💰")

    if "goods_list" not in st.session_state:
        st.session_state.goods_list = []

    with st.sidebar:
        st.header("📦 商品参数")
        prod_cat = st.selectbox("产品种类", PROD_CATEGORY, key="cat")

        if prod_cat == "wig":
            wig_bundle_grade = st.selectbox("Wig 发帘等级", BUNDLE_GRADES, key="wig_bundle")
            wig_base_type = st.selectbox("Wig 发块类型", WIG_BASE_TYPE, key="wig_type")
            wig_base_grade = st.selectbox("Wig 发块等级", CLOSURE_GRADES if wig_base_type=="closure" else FRONTAL_GRADES, key="wig_grade")
            density = st.selectbox("Wig 密度", WIG_DENS_LIST, key="dens")
            base_g = GRADE_BASE_MAP.get(wig_bundle_grade, wig_bundle_grade)
            wave_list = GRADE_ALLOW_WAVE.get(base_g, [])
            wave = st.selectbox("波度", wave_list, key="wave_wig")
            grade_for_price = wig_bundle_grade
            is_wig = True
        else:
            if prod_cat == "bundle":
                grade_list = BUNDLE_GRADES
            elif prod_cat == "closure":
                grade_list = CLOSURE_GRADES
            else:
                grade_list = FRONTAL_GRADES
            grade = st.selectbox("产品等级", grade_list, key="grade")
            base_g = GRADE_BASE_MAP.get(grade, grade)
            wave_list = GRADE_ALLOW_WAVE.get(base_g, [])
            wave = st.selectbox("波度", wave_list, key="wave_normal")
            grade_for_price = grade
            is_wig = False

        length_str = st.text_input("长度（逗号分隔，如 12,14,16）", value="12", key="len")
        qty = st.number_input("数量", min_value=1, value=1, step=1, key="qty")
        country = st.selectbox("客户国家", COUNTRY_LIST, key="country")
        pay = st.selectbox("付款方式", PAY_LIST, key="pay")
        tier_label = st.selectbox("价格档位", PRICE_TIER_LIST, key="tier")
        tier = "vip" if "VIP" in tier_label else "retail"
        ship_mode = st.radio("运费模式", ["正常运费", "最低运费"], index=0, key="ship")
        ship_key = "reg" if ship_mode == "正常运费" else "low"

        if st.button("➕ 添加商品", use_container_width=True):
            try:
                lengths = [int(x.strip()) for x in length_str.split(",") if x.strip()]
            except:
                st.error("长度请输入数字，用逗号分隔")
                st.stop()
            if not lengths:
                st.error("至少输入一个长度")
                st.stop()

            for l in lengths:
                if is_wig:
                    unit = calc_wig_total_cost(wig_bundle_grade, wig_base_type, wig_base_grade, density, l, wave, tier)
                    prod_name = f"Wig-{density}密度-{wig_base_type}({wig_base_grade})"
                else:
                    unit = calc_normal_price(prod_cat, grade_for_price, wave, l, tier)
                    prod_name = f"{prod_cat}({grade_for_price})"
                if unit <= 0:
                    st.error(f"{prod_name} {l}寸无价格，请检查规格")
                    st.stop()
                sub = round(unit * qty, 2)
                item = {
                    "full_name": prod_name,
                    "wave": wave,
                    "length": l,
                    "qty": qty,
                    "unit": unit,
                    "sub": sub,
                    "country": country,
                    "pay": pay,
                    "tier": tier
                }
                st.session_state.goods_list.append(item)
            st.success(f"已添加 {len(lengths)} 项商品")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("📋 已添加商品明细")
        if not st.session_state.goods_list:
            st.info("购物车为空")
        else:
            import pandas as pd
            df = pd.DataFrame(st.session_state.goods_list)
            df_display = df[["full_name", "wave", "length", "qty", "unit", "sub"]]
            df_display.columns = ["商品", "波度", "长度(in)", "数量", "单价($)", "小计($)"]
            st.dataframe(df_display, use_container_width=True)

            del_idx = st.number_input("删除行号（从1开始）", min_value=1, max_value=len(st.session_state.goods_list), step=1, key="del_idx")
            if st.button("🗑️ 删除该行"):
                idx = del_idx - 1
                if 0 <= idx < len(st.session_state.goods_list):
                    del st.session_state.goods_list[idx]
                    st.experimental_rerun()
            if st.button("🗑️ 清空全部"):
                st.session_state.goods_list.clear()
                st.experimental_rerun()

    with col2:
        st.subheader("📊 生成报价")
        if st.button("📊 生成报价单", use_container_width=True):
            if not st.session_state.goods_list:
                st.warning("请先添加商品")
            else:
                total_goods = sum(item["sub"] for item in st.session_state.goods_list)
                total_qty = sum(item["qty"] for item in st.session_state.goods_list)
                total_w = 0
                for it in st.session_state.goods_list:
                    if "Wig" in it["full_name"]:
                        if "180" in it["full_name"]:
                            w = 400
                        elif "250" in it["full_name"]:
                            w = 500
                        else:
                            w = 600
                    else:
                        w = 100
                    total_w += w * it["qty"]
                country = st.session_state.goods_list[0]["country"]
                paytype = st.session_state.goods_list[0]["pay"]
                ship = get_ship_fee(total_w, country, ship_key)
                st.markdown("---")
                st.write(f"**总数量 (Total quantity):** {total_qty}")
                st.write(f"**商品总金额 (Goods cost):** ${total_goods:.2f}")
                st.write(f"**包裹总重量 (Total weight):** {total_w} g")
                if ship is not None:
                    st.write(f"**国际运费 (Shipping cost):** ${ship:.2f}")
                    base = total_goods + ship
                    rate = PAYPAL_RATE if "PayPal" in paytype else ALIBABA_RATE
                    fee = round(base * rate, 2)
                    final = round(base + fee, 2)
                    st.write(f"**货值+运费 (Goods + Shipping):** ${base:.2f}")
                    st.write(f"**手续费 ({rate*100:.1f}%):** ${fee:.2f}")
                    st.success(f"**最终应付总金额 (Final total):** ${final:.2f}")
                else:
                    st.error(f"⚠️ 总重量 {total_w}g 无匹配运费档位！")

                with st.expander("📄 完整报价单文本"):
                    st.text("="*80)
                    st.text("订单明细")
                    st.text("-"*80)
                    for it in st.session_state.goods_list:
                        st.text(f"{it['full_name']} | Wave:{it['wave']} | Len:{it['length']}in | ${it['unit']:.2f} x{it['qty']} = ${it['sub']:.2f}")
                    st.text("\n" + "="*80)
                    st.text("费用汇总")
                    st.text("-"*80)
                    st.text(f"总数量 (Total quantity): {total_qty}")
                    st.text(f"商品总金额 (Goods cost): ${total_goods:.2f}")
                    st.text(f"包裹总重量 (Total weight): {total_w} g")
                    if ship is not None:
                        st.text(f"国际运费 (Shipping cost): ${ship:.2f}")
                        st.text(f"货值+运费 (Goods + Shipping): ${base:.2f}")
                        st.text(f"手续费 ({rate*100:.1f}%): ${fee:.2f}")
                        st.text(f"\n最终应付总金额 (Final total): ${final:.2f}")
                    st.text("="*80)

if __name__ == "__main__":
    main()
