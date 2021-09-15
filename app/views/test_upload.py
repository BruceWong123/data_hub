import requests
from pathlib import Path
import os
import json
from pymongo import MongoClient

import labeling.perception_labeling_rosbag_parser_pb2 as perception_labeling

# from celery import Celery
import requests
import base64


class Test_UPload:
    def __init__(self):
        print("init")
        pass

    def upload_labeling(self):
        service_end_point = "http://127.0.0.1:8000/api/"
        upload_url = service_end_point + "labeling/time/upload/"

        data = "{\"8\": {\"timestamp\": {\"objects\": 1584360195850000, \"camera6\": 1584360195883748838, \"camera2\": 1584360195916826862, \"camera1\": 1584360195900073653}, \"rostime\": {\"objects\": \"1584360196018079\", \"camera6\": \"1584360195903940\", \"camera2\": \"1584360195939053\", \"camera1\": \"1584360195922630\"}}, \"9\": {\"timestamp\": {\"objects\": 1584360195950000, \"camera6\": 1584360195983747510, \"camera2\": 1584360196016829070, \"camera1\": 1584360196000116133}, \"rostime\": {\"objects\": \"1584360196117999\", \"camera6\": \"1584360196004368\", \"camera2\": \"1584360196038858\", \"camera1\": \"1584360196023211\"}}}"
        # data = json.loads(data)

        index_data = "{\"/perception/objects\": \"{0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 11: 12, 12: 13, 13: 14, 14: 15, 15: 16, 16: 17, 17: 18, 18: 19, 19: 20, 20: 21, 21: 22, 22: 23, 23: 24, 24: 25, 25: 26, 26: 27, 27: 28, 28: 29, 29: 30, 30: 31, 31: 32, 32: 33, 33: 34, 34: 35, 35: 36, 36: 37, 37: 38, 38: 39, 39: 40, 40: 41, 41: 42, 42: 43, 43: 44, 44: 45, 45: 46, 46: 47, 47: 48, 48: 49, 49: 50, 50: 51, 51: 52, 52: 53, 53: 54, 54: 55, 55: 56, 56: 57, 57: 58, 58: 59, 59: 60, 60: 61, 61: 62, 62: 63, 63: 64, 64: 65, 65: 66, 66: 67, 67: 68, 68: 69, 69: 70, 70: 71, 71: 72, 72: 73, 73: 74, 74: 75, 75: 76, 76: 77, 77: 78, 78: 79, 79: 80, 80: 81, 81: 82, 82: 83, 83: 84, 84: 85, 85: 86, 86: 87, 87: 88, 88: 89, 89: 90, 90: 91, 91: 92, 92: 93, 93: 94, 94: 95, 95: 96, 96: 97, 97: 98, 98: 99, 99: 100, 100: 101, 101: 102, 102: 103, 103: 104, 104: 105, 105: 106, 106: 107, 107: 108, 108: 109, 109: 110, 110: 111, 111: 112, 112: 113, 113: 114, 114: 115, 115: 116, 116: 117, 117: 118, 118: 119, 119: 120, 120: 121, 121: 122, 122: 123, 123: 124, 124: 125, 125: 126, 126: 127, 127: 128, 128: 129, 129: 130, 130: 131, 131: 132, 132: 133, 133: 134, 134: 135, 135: 136, 136: 137, 137: 138, 138: 139, 139: 140, 140: 141, 141: 142, 142: 143, 143: 144, 144: 145, 145: 146, 146: 147, 147: 148, 148: 149, 149: 150, 150: 151, 151: 152, 152: 153, 153: 154, 154: 155, 155: 156, 156: 157, 157: 158, 158: 159, 159: 160, 160: 161, 161: 162, 162: 163, 163: 164, 164: 165, 165: 166, 166: 167, 167: 168, 168: 169, 169: 170, 170: 171, 171: 172, 172: 173, 173: 174, 174: 175, 175: 176, 176: 177, 177: 178, 178: 179, 179: 180, 180: 181, 181: 182, 182: 183, 183: 184, 184: 185, 185: 186, 186: 187, 187: 188, 188: 189, 189: 190, 190: 191, 191: 192, 192: 193, 193: 194, 194: 195, 195: 196, 196: 197, 197: 198, 198: 199, 199: 200, 200: 201, 201: 202, 202: 203, 203: 204, 204: 205, 205: 206, 206: 207, 207: 208, 208: 209, 209: 210, 210: 211, 211: 212, 212: 213, 213: 214, 214: 215, 215: 216, 216: 217, 217: 218, 218: 219, 219: 220, 220: 221, 221: 222, 222: 223, 223: 224, 224: 225, 225: 226, 226: 227, 227: 228, 228: 229, 229: 230, 230: 231, 231: 232, 232: 233, 233: 234, 234: 235, 235: 236, 236: 237, 237: 238, 238: 239, 239: 240, 240: 241, 241: 242, 242: 243, 243: 244, 244: 245, 245: 246, 246: 247, 247: 248, 248: 249, 249: 250, 250: 251, 251: 252, 252: 253, 253: 254, 254: 255, 255: 256, 256: 257, 257: 258, 258: 259, 259: 260, 260: 261, 261: 262, 262: 263, 263: 264, 264: 265, 265: 266, 266: 267, 267: 268, 268: 269, 269: 270, 270: 271, 271: 272, 272: 273, 273: 274, 274: 275, 275: 276, 276: 277, 277: 278, 278: 279, 279: 280, 280: 281, 281: 282, 282: 283, 283: 284, 284: 285, 285: 286, 286: 287, 287: 288, 288: 289, 289: 290, 290: 291, 291: 292, 292: 293, 293: 294, 294: 295, 295: 296, 296: 297, 297: 298, 298: 299, 299: 300, 300: 301, 301: 302, 302: 303, 303: 304, 304: 305, 305: 306, 306: 307, 307: 308, 308: 309, 309: 310, 310: 311, 311: 312, 312: 313, 313: 314, 314: 315, 315: 316, 316: 317, 317: 318, 318: 319, 319: 320, 320: 321, 321: 322, 322: 323, 323: 324, 324: 325, 325: 326, 326: 327, 327: 328, 328: 329, 329: 330, 330: 331, 331: 332, 332: 333, 333: 334, 334: 335, 335: 336, 336: 337, 337: 338, 338: 339, 339: 340, 340: 341, 341: 342, 342: 343, 343: 344, 344: 345, 345: 346, 346: 347, 347: 348, 348: 349}\", \"/sensors/camera/camera_2_raw_data\": \"{0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13, 14: 14, 15: 15, 16: 16, 17: 17, 18: 18, 19: 19, 20: 20, 21: 21, 22: 22, 23: 23, 24: 24, 25: 25, 26: 26, 27: 27, 28: 28, 29: 29, 30: 30, 31: 31, 32: 32, 33: 33, 34: 34, 35: 35, 36: 36, 37: 37, 38: 38, 39: 39, 40: 40, 41: 41, 42: 42, 43: 43, 44: 44, 45: 45, 46: 46, 47: 47, 48: 48, 49: 49, 50: 50, 51: 51, 52: 52, 53: 53, 54: 54, 55: 55, 56: 56, 57: 57, 58: 58, 59: 59, 60: 60, 61: 61, 62: 62, 63: 63, 64: 64, 65: 65, 66: 66, 67: 67, 68: 68, 69: 69, 70: 70, 71: 71, 72: 72, 73: 73, 74: 74, 75: 75, 76: 76, 77: 77, 78: 78, 79: 79, 80: 80, 81: 81, 82: 82, 83: 83, 84: 84, 85: 85, 86: 86, 87: 87, 88: 88, 89: 89, 90: 90, 91: 91, 92: 92, 93: 93, 94: 94, 95: 95, 96: 96, 97: 97, 98: 98, 99: 99, 100: 100, 101: 101, 102: 102, 103: 103, 104: 104, 105: 105, 106: 106, 107: 107, 108: 108, 109: 109, 110: 110, 111: 111, 112: 112, 113: 113, 114: 114, 115: 115, 116: 116, 117: 117, 118: 118, 119: 119, 120: 120, 121: 121, 122: 122, 123: 123, 124: 124, 125: 125, 126: 126, 127: 127, 128: 128, 129: 129, 130: 130, 131: 131, 132: 132, 133: 133, 134: 134, 135: 135, 136: 136, 137: 137, 138: 138, 139: 139, 140: 140, 141: 141, 142: 142, 143: 143, 144: 144, 145: 145, 146: 146, 147: 147, 148: 148, 149: 149, 150: 150, 151: 151, 152: 152, 153: 153, 154: 154, 155: 155, 156: 156, 157: 157, 158: 158, 159: 159, 160: 160, 161: 161, 162: 162, 163: 163, 164: 164, 165: 165, 166: 166, 167: 167, 168: 168, 169: 169, 170: 170, 171: 171, 172: 172, 173: 173, 174: 174, 175: 175, 176: 176, 177: 177, 178: 178, 179: 179, 180: 180, 181: 181, 182: 182, 183: 183, 184: 184, 185: 185, 186: 186, 187: 187, 188: 188, 189: 189, 190: 190, 191: 191, 192: 192, 193: 193, 194: 194, 195: 195, 196: 196, 197: 197, 198: 198, 199: 199, 200: 200, 201: 201, 202raw_data, 252: 252, 253: 253, 254: 254, 255: 255, 256: 256, 257: 257, 258: 258, 259: 259, 260: 260, 261: 261, 262: 262, 263: 263, 264: 264, 265: 265, 266: 266, 267: 267, 268: 268, 269: 269, 270: 270, 271: 271, 272: 272, 273: 273, 274: 274, 275: 275, 276: 276, 277: 277, 278: 278, 279: 279, 280: 280, 281: 281, 282: 282, 283: 283, 284: 284, 285: 285, 286: 286, 287: 287, 288: 288, 289: 289, 290: 290, 291: 291, 292: 292, 293: 293, 294: 294, 295: 295, 296: 296, 297: 297, 298: 298, 299: 299, 300: 300, 301: 301, 302: 302, 303: 303, 304: 304, 305: 305, 306: 306, 307: 307, 308: 308, 309: 309, 310: 310, 311: 311, 312: 312, 313: 313, 314: 314, 315: 315, 316: 316, 317: 317, 318: 318, 319: 319, 320: 320, 321: 321, 322: 322, 323: 323, 324: 324, 325: 325, 326: 326, 327: 327, 328: 328, 329: 329, 330: 330, 331: 331, 332: 332, 333: 333, 334: 334, 335: 335, 336: 336, 337: 337, 338: 338, 339: 339, 340: 340, 341: 341, 342: 342, 343: 343, 344: 344, 345: 345, 346: 346, 347: 347, 348: 348}\", \"/sensors/camera/camera_1_raw_data\": \"{0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13, 14: 14, 15: 15, 16: 16, 17: 17, 18: 18, 19: 19, 20: 20, 21: 21, 22: 22, 23: 23, 24: 24, 25: 25, 26: 26, 27: 27, 28: 28, 29: 29, 30: 30, 31: 31, 32: 32, 33: 33, 34: 34, 35: 35, 36: 36, 37: 37, 38: 38, 39: 39, 40: 40, 41: 41, 42: 42, 43: 43, 44: 44, 45: 45, 46: 46, 47: 47, 48: 48, 49: 49, 50: 50, 51: 51, 52: 52, 53: 53, 54: 54, 55: 55, 56: 56, 57: 57, 58: 58, 59: 59, 60: 60, 61: 61, 62: 62, 63: 63, 64: 64, 65: 65, 66: 66, 67: 67, 68: 68, 69: 69, 70: 70, 71: 71, 72: 72, 73: 73, 74: 74, 75: 75, 76: 76, 77: 77, 78: 78, 79: 79, 80: 80, 81: 81, 82: 82, 83: 83, 84: 84, 85: 85, 86: 86, 87: 87, 88: 88, 89: 89, 90: 90, 91: 91, 92: 92, 93: 93, 94: 94, 95: 95, 96: 96, 97: 97, 98: 98, 99: 99, 100: 100, 101: 101, 102: 102, 103: 103, 104: 104, 105: 105, 106: 106, 107: 107, 108: 108, 109: 109, 110: 110, 111: 111, 112: 112, 113: 113, 114: 114, 115: 115, 116: 116, 117: 117, 118: 118, 119: 119, 120: 120, 121: 121, 122: 122, 123: 123, 124: 124, 125: 125, 126: 126, 127: 127, 128: 128, 129: 129, 130: 130, 131: 131, 132: 132, 133: 133, 134: 134, 135: 135, 136: 136, 137: 137, 138: 138, 139: 139, 140: 140, 141: 141, 142: 142, 143: 143, 144: 144, 145: 145, 146: 146, 147: 147, 148: 148, 149: 149, 150: 150, 151: 151, 152: 152, 153: 153, 154: 154, 155: 155, 156: 156, 157: 157, 158: 158, 159: 159, 160: 160, 161: 161, 162: 162, 163: 163, 164: 164, 165: 165, 166: 166, 167: 167, 168: 168, 169: 169, 170: 170, 171: 171, 172: 172, 173: 173, 174: 174, 175: 175, 176: 176, 177: 177, 178: 178, 179: 179, 180: 180, 181: 181, 182: 182, 183: 183, 184: 184, 185: 185, 186: 186, 187: 187, 188: 188, 189: 189, 190: 190, 191: 191, 192: 192, 193: 193, 194: 194, 195: 195, 196: 196, 197: 197, 198: 198, 199: 199, 200: 200, 201: 201, 202: 202, 203: 203, 204: 204, 205: 205, 206: 206, 207: 207, 208: 208, 209: 209, 210: 210, 211: 211, 212: 212, 213: 213, 214: 214, 215: 215, 216: 216, 217: 217, 218: 218, 219: 219, 220: 220, 221: 221, 222: 222, 223: 223, 224: 224, 225: 225, 226: 226, 227: 227, 228: 228, 229: 229, 230: 230, 231: 231, 232: 232, 233: 233, 234: 234, 235: 235, 236: 236, 237: 237, 238: 238, 239: 239, 240: 240, 241: 241, 242: 242, 243: 243, 244: 244, 245: 245, 246: 246, 247: 247, 248: 248, 249: 249, 250: 250, 251: 251, 252: 252, 253: 253, 254: 254, 255: 255, 256: 256, 257: 257, 258: 258, 259: 259, 260: 260, 261: 261, 262: 262, 263: 263, 264: 264, 265: 265, 266: 266, 267: 267, 268: 268, 269: 269, 270: 270, 271: 271, 272: 272, 273: 273, 274: 274, 275: 275, 276: 276, 277: 277, 278: 278, 279: 279, 280: 280, 281: 281, 282: 282, 283: 283, 284: 284, 285: 285, 286: 286, 287: 287, 288: 288, 289: 289, 290: 290, 291: 291, 292: 292, 293: 293, 294: 294, 295: 295, 296: 296, 297: 297, 298: 298, 299: 299, 300: 300, 301: 301, 302: 302, 303: 303, 304: 304, 305: 305, 306: 306, 307: 307, 308: 308, 309: 309, 310: 310, 311: 311, 312: 312, 313: 313, 314: 314, 315: 315, 316: 316, 317: 317, 318: 318, 319: 319, 320: 320, 321: 321, 322: 322, 323: 323, 324: 324, 325: 325, 326: 326, 327: 327, 328: 328, 329: 329, 330: 330, 331: 331, 332: 332, 333: 333, 334: 334, 335: 335, 336: 336, 337: 337, 338: 338, 339: 339, 340: 340, 341: 341, 342: 342, 343: 343, 344: 344, 345: 345, 346: 346, 347: 347, 348: 348}\", \"/sensors/camera/camera_6_raw_data\": \"{0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13, 14: 14, 15: 15, 16: 16, 17: 17, 18: 18, 19: 19, 20: 20, 21: 21, 22: 22, 23: 23, 24: 24, 25: 25, 26: 26, 27: 27, 28: 28, 29: 29, 30: 30, 31: 31, 32: 32, 33: 33, 34: 34, 35: 35, 36: 36, 37: 37, 38: 38, 39: 39, 40: 40, 41: 41, 42: 42, 43: 43, 44: 44, 45: 45, 46: 46, 47: 47, 48: 48, 49: 49, 50: 50, 51: 51, 52: 52, 53: 53, 54: 54, 55: 55, 56: 56, 57: 57, 58: 58, 59: 59, 60: 60, 61: 61, 62: 62, 63: 63, 64: 64, 65: 65, 66: 66, 67: 67, 68: 68, 69: 69, 70: 70, 71: 71, 72: 72, 73: 73, 74: 74, 75: 75, 76: 76, 77: 77, 78: 78, 79: 79, 80: 80, 81: 81, 82: 82, 83: 83, 84: 84, 85: 85, 86: 86, 87: 87, 88: 88, 89: 89, 90: 90, 91: 91, 92: 92, 93: 93, 94: 94, 95: 95, 96: 96, 97: 97, 98: 98, 99: 99, 100: 100, 101: 101, 102: 102, 103: 103, 104: 104, 105: 105, 106: 106, 107: 107, 108: 108, 109: 109, 110: 110, 111: 111, 112: 112, 113: 113, 114: 114, 115: 115, 116: 116, 117: 117, 118: 118, 119: 119, 120: 120, 121: 121, 122: 122, 123: 123, 124: 124, 125: 125, 126: 126, 127: 127, 128: 128, 129: 129, 130: 130, 131: 131, 132: 132, 133: 133, 134: 134, 135: 135, 136: 136, 137: 137, 138: 138, 139: 139, 140: 140, 141: 141, 142: 142, 143: 143, 144: 144, 145: 145, 146: 146, 147: 147, 148: 148, 149: 149, 150: 150, 151: 151, 152: 152, 153: 153, 154: 154, 155: 155, 156: 156, 157: 157, 158: 158, 159: 159, 160: 160, 161: 161, 162: 162, 163: 163, 164: 164, 165: 165, 166: 166, 167: 167, 168: 168, 169: 169, 170: 170, 171: 171, 172: 172, 173: 173, 174: 174, 175: 175, 176: 176, 177: 177, 178: 178, 179: 179, 180: 180, 181: 181, 182: 182, 183: 183, 184: 184, 185: 185, 186: 186, 187: 187, 188: 188, 189: 189, 190: 190, 191: 191, 192: 192, 193: 193, 194: 194, 195: 195, 196: 196, 197: 197, 198: 198, 199: 199, 200: 200, 201: 201, 202: 202, 203: 203, 204: 204, 205: 205, 206: 206, 207: 207, 208: 208, 209: 209, 210: 210, 211: 211, 212: 212, 213: 213, 214: 214, 215: 215, 216: 216, 217: 217, 218: 218, 219: 219, 220: 220, 221: 221, 222: 222, 223: 223, 224: 224, 225: 225, 226: 226, 227: 227, 228: 228, 229: 229, 230: 230, 231: 231, 232: 232, 233: 233, 234: 234, 235: 235, 236: 236, 237: 237, 238: 238, 239: 239, 240: 240, 241: 241, 242: 242, 243: 243, 244: 244, 245: 245, 246: 246, 247: 247, 248: 248, 249: 249, 250: 250, 251: 251, 252: 252, 253: 253, 254: 254, 255: 255, 256: 256, 257: 257, 258: 258, 259: 259, 260: 260, 261: 261, 262: 262, 263: 263, 264: 264, 265: 265, 266: 266, 267: 267, 268: 268, 269: 269, 270: 270, 271: 271, 272: 272, 273: 273, 274: 274, 275: 275, 276: 276, 277: 277, 278: 278, 279: 279, 280: 280, 281: 281, 282: 282, 283: 283, 284: 284, 285: 285, 286: 286, 287: 287, 288: 288, 289: 289, 290: 290, 291: 291, 292: 292, 293: 293, 294: 294, 295: 295, 296: 296, 297: 297, 298: 298, 299: 299, 300: 300, 301: 301, 302: 302, 303: 303, 304: 304, 305: 305, 306: 306, 307: 307, 308: 308, 309: 309, 310: 310, 311: 311, 312: 312, 313: 313, 314: 314, 315: 315, 316: 316, 317: 317, 318: 318, 319: 319, 320: 320, 321: 321, 322: 322, 323: 323, 324: 324, 325: 325, 326: 326, 327: 327, 328: 328, 329: 329, 330: 330, 331: 331, 332: 332, 333: 333, 334: 334, 335: 335, 336: 336, 337: 337, 338: 338, 339: 339, 340: 340, 341: 341, 342: 342, 343: 343, 344: 344, 345: 345, 346: 346, 347: 347, 348: 348}\"}"

        time_data = "{\"348\": {\"timestamp\": \"{'objects': 1584360195850000, '/sensors/camera/camera_6_raw_data': 1584360195883748838, '/sensors/camera/camera_2_raw_data': 1584360195916826862, '/sensors/camera/camera_1_raw_data': 1584360195900073653}\", \"rostime\": \"{'objects': 1584360196018079, '/sensors/camera/camera_6_raw_data': 1584360195903940, '/sensors/camera/camera_2_raw_data': 1584360195939053, '/sensors/camera/camera_1_raw_data': 1584360195922630}\"}, \"349\": {\"timestamp\": \"{'objects': 1584360195950000, '/sensors/camera/camera_6_raw_data': 1584360195983747510, '/sensors/camera/camera_2_raw_data': 1584360196016829070, '/sensors/camera/camera_1_raw_data': 1584360196000116133}\", \"rostime\": \"{'objects': 1584360196117999, '/sensors/camera/camera_6_raw_data': 1584360196004368, '/sensors/camera/camera_2_raw_data': 1584360196038858, '/sensors/camera/camera_1_raw_data': 1584360196023211}\"}}"

        data_dict = {}
        data_dict["data"] = time_data
        data_dict["bagid"] = "YR_MKZ_1_20201207_022851_755_40"
        session = requests.session()
        session.keep_alive = False
        print(data_dict)
        session.put(url=upload_url, data=data_dict)
        print("upload done")

    def upload_labeling_data2(self):
        # service_end_point = "http://127.0.0.1:8000/api/"
        service_end_point = "http://dataserver.prediction.simulation.deeproute.ai/api/"
        upload_url = service_end_point + "labeling/data/first_upload/"
        data_dict = {}
        data_dict["data"] = "annotation dfa222fffffasdf"
        data_dict["bagId"] = "YR_MKZ_1_20210105"
        data_dict["frameId"] = 22
        data_dict["timestamp"] = "testtest"
        frame_fields = []
        frame_fields.append("object_2d")
        data_dict["frameFields"] = frame_fields
        print(data_dict)
        session = requests.session()
        session.keep_alive = False
        print("send request")
        session.put(url=upload_url, data=data_dict)
        print("done")

    def upload_labeling_data(self):
        service_end_point = "http://127.0.0.1:8000/api/"

        # service_end_point = "http://dataserver.prediction.simulation.deeproute.ai/api/"
        upload_url = service_end_point + "labeling/data/upload/"
        data_dict = {}
        data_dict["data"] = "annotation dfa222fffffasdf"
        data_dict["bagId"] = "YR_MKZ_1_20210105_biandao_PM2"
        data_dict["frameId"] = 98
        data_dict["timestamp"] = "0"
        frame_fields = []
        frame_fields.append("object_2d")
        data_dict["frameFields"] = frame_fields
        print(data_dict)
        session = requests.session()
        session.keep_alive = False
        print("send request")
        session.put(url=upload_url, data=data_dict)
        print("done")

    def download_labeling_data(self):
        # service_end_point = "http://127.0.0.1:8000/api/"
        service_end_point = "http://dataserver.prediction.simulation.deeproute.ai/api/"
        upload_url = service_end_point + "labeling/data/download/"

        data_dict = dict()
        data_dict["bagId"] = "YR_MKZ_1_20210105_biandao_PM2"
        data_dict["frameId"] = 0
        data_dict["timestamp"] = "0"
        frame_fields = []
        frame_fields.append("object_3d")
        data_dict["frameFields"] = frame_fields

        session = requests.session()
        session.keep_alive = False
        result = session.put(url=upload_url, data=data_dict)
        print(result)

    def download_trajectory_data(self):
        # service_end_point = "http://127.0.0.1:8000/api/"
        service_end_point = "http://dataserver.prediction.simulation.deeproute.ai/api/"
        upload_url = service_end_point + "trajectory/data/is_still/50/"

        session = requests.session()
        session.keep_alive = False
        result = session.get(url=upload_url)
        print(result.text)

    def download_trajectory_data(self):
        # service_end_point = "http://127.0.0.1:8000/api/"
        service_end_point = "http://dataserver.prediction.simulation.deeproute.ai/api/"
        upload_url = service_end_point + "trajectory/data/download/"

        data_dict = dict()
        data_dict["attributes"] = "{[\"is_still\"]}"
        session = requests.session()
        session.keep_alive = False
        result = session.put(url=upload_url, data=data_dict)
        print(result)

    def download_trajectory_data_multiattributes(self):
        # service_end_point = "http://127.0.0.1:8000/api/"
        service_end_point = "http://dataserver.prediction.simulation.deeproute.ai/api/"
        upload_url = service_end_point + "trajectory/data/multiattributes/download/"

        data_dict = dict()
        data_dict["is_still"] = "true"
        data_dict["on_lane"] = "false"
        session = requests.session()
        session.keep_alive = False
        result = session.put(url=upload_url, data=data_dict)
        print(result.text)

    def upload_attributes(self):
        # service_end_point = "http://127.0.0.1:8000/api/"
        service_end_point = "http://dataserver.prediction.simulation.deeproute.ai/api/"
        upload_url = service_end_point + "trajectory/attributes/upload/"

        data = "[{\"timestamp\": \"1580604436850000\", \"attribute\":[ {\"object_id\": \"32663\", \"turn\": \"false\", \"is_still\": \"true\", \"on_lane\": \"false\", \"lane_change\": \"true\", \"on_crosswalk\": \"true\", \"in_junction\": \"false\"}, {\"object_id\": \"32661\", \"turn\": \"false\", \"is_still\": \"true\", \"on_lane\": \"false\", \"lane_change\": \"true\", \"on_crosswalk\": \"true\", \"in_junction\": \"false\"}]},{\"timestamp\": \"1580604436860000\", \"attribute\":[ {\"object_id\": \"32663\", \"turn\": \"false\", \"is_still\": \"true\", \"on_lane\": \"false\", \"lane_change\": \"true\", \"on_crosswalk\": \"true\", \"in_junction\": \"false\"}, {\"object_id\": \"32661\", \"turn\": \"false\", \"is_still\": \"true\", \"on_lane\": \"false\", \"lane_change\": \"true\", \"on_crosswalk\": \"true\", \"in_junction\": \"false\"}]},{\"timestamp\": \"1580604436880000\", \"attribute\":[ {\"object_id\": \"32663\", \"turn\": \"false\", \"is_still\": \"true\", \"on_lane\": \"false\", \"lane_change\": \"true\", \"on_crosswalk\": \"true\", \"in_junction\": \"false\"}, {\"object_id\": \"32661\", \"turn\": \"false\", \"is_still\": \"true\", \"on_lane\": \"false\", \"lane_change\": \"true\", \"on_crosswalk\": \"true\", \"in_junction\": \"false\"}]}]"
        data_dict = {}
        data_dict["data"] = data
        data_dict["bagId"] = "YR_MKZ_1_20201207_022851_755_40_test"
        session = requests.session()
        session.keep_alive = False
        print(data_dict)
        session.put(url=upload_url, data=data_dict)
        print("upload done")

    def upload_trajectory(self, filename):
        # service_end_point = "http://127.0.0.1:8000/api/"
        service_end_point = "http://dataserver.prediction.simulation.deeproute.ai/api/"
        upload_url = service_end_point + "trajectory/upload/"

        data = ""
        with open(filename, "r", encoding="utf-8") as f:
            for line in f.readlines():
                line = line.strip()
                data += " "
                data += line

        data_dict = {}
        data_dict["data"] = data
        data_dict["bagid"] = "YR_MKZ_1_20201207_022851_755_40"
        session = requests.session()
        session.keep_alive = False
        # print(data)
        session.put(url=upload_url, data=data_dict)
        print("download done")

    def upload_trajectory_by_dict(self):
        # service_end_point = "http://127.0.0.1:8000/api/"
        service_end_point = "http://dataserver.prediction.simulation.deeproute.ai/api/"
        upload_url = service_end_point + "trajectory/upload/"

        data = "{\"trajectory\": [{\"perception_object_id\": \"1111\", \"timestamp\": \"2323232\",      \"perception_obj_type\": \"xxx\",\"x\": \"1111\",\"y\": \"2222\",\"z\": \"3333\",\"l\": \"333\",   \"w\": \"333\",\"h\": \"45\",\"theta\": \"1111\",\"v_x\": \"2222\",\"v_y\": \"3333\",\"a_x\": \"333\",\"a_y\": \"333\",\"is_still\": \"false\",\"lane_s\": \"1111\",\"lane_l\": \"2222\",      \"dist_to_left_boundary\": \"3333\",\"dist_to_right_boundary\": \"3333\",\"lane_sequences\": \"3333\"}, {\"perception_object_id\": \"262433\", \"timestamp\": \"2323232\",      \"perception_obj_type\": \"xxx\",\"x\": \"1111\",\"y\": \"2222\",\"z\": \"3333\",\"l\": \"333\",   \"w\": \"333\",\"h\": \"45\",\"theta\": \"1111\",\"v_x\": \"2222\",\"v_y\": \"3333\",\"a_x\": \"333\",\"a_y\": \"333\",\"is_still\": \"false\",\"lane_s\": \"1111\",\"lane_l\": \"2222\",      \"dist_to_left_boundary\": \"3333\",\"dist_to_right_boundary\": \"3333\",\"lane_sequences\": \"3333\"},{\"perception_object_id\": \"262633\", \"timestamp\": \"2323232\",      \"perception_obj_type\": \"xxx\",\"x\": \"1111\",\"y\": \"2222\",\"z\": \"3333\",\"l\": \"333\",   \"w\": \"333\",\"h\": \"45\",\"theta\": \"1111\",\"v_x\": \"2222\",\"v_y\": \"3333\",\"a_x\": \"333\",\"a_y\": \"333\",\"is_still\": \"false\",\"lane_s\": \"1111\",\"lane_l\": \"2222\",      \"dist_to_left_boundary\": \"3333\",\"dist_to_right_boundary\": \"3333\",\"lane_sequences\": \"3333\"}]}"

        data_dict = {}
        data_dict["data"] = data
        data_dict["bagId"] = "test_test_test_test_test"
        session = requests.session()
        session.keep_alive = False
        # print(data)
        result = session.put(url=upload_url, data=data_dict)
        print(result)
        print("upload done")

    def upload_object_info(self):
        # service_end_point = "http://127.0.0.1:8000/api/"
        service_end_point = "http://dataserver.prediction.simulation.deeproute.ai/api/"
        upload_url = service_end_point + "object_info/upload/"

        data = "{\"bagId\": \" test_test_frame_info\",\"perception_object_id\": \"1111\",\"trajectory\": [{ \"timestamp\": \"2323232\",  \"perception_obj_type\": \"xxx\",\"x\": \"1111\",\"y\": \"2222\",\"z\": \"3333\",\"l\": \"333\",   \"w\": \"333\",\"h\": \"45\",\"theta\": \"1111\",\"v_x\": \"2222\",\"v_y\": \"3333\",\"a_x\": \"333\",\"a_y\": \"333\",\"is_still\": \"false\",\"lane_s\": \"1111\",\"lane_l\": \"2222\",      \"dist_to_left_boundary\": \"3333\",\"dist_to_right_boundary\": \"3333\",\"lane_sequences\": \"3333\"}, {\"timestamp\": \"2323232\",      \"perception_obj_type\": \"xxx\",\"x\": \"1111\",\"y\": \"2222\",\"z\": \"3333\",\"l\": \"333\",   \"w\": \"333\",\"h\": \"45\",\"theta\": \"1111\",\"v_x\": \"2222\",\"v_y\": \"3333\",\"a_x\": \"333\",\"a_y\": \"333\",\"is_still\": \"false\",\"lane_s\": \"1111\",\"lane_l\": \"2222\",      \"dist_to_left_boundary\": \"3333\",\"dist_to_right_boundary\": \"3333\",\"lane_sequences\": \"3333\"},{ \"timestamp\": \"2323232\",      \"perception_obj_type\": \"xxx\",\"x\": \"1111\",\"y\": \"2222\",\"z\": \"3333\",\"l\": \"333\",   \"w\": \"333\",\"h\": \"45\",\"theta\": \"1111\",\"v_x\": \"2222\",\"v_y\": \"3333\",\"a_x\": \"333\",\"a_y\": \"333\",\"is_still\": \"false\",\"lane_s\": \"1111\",\"lane_l\": \"2222\",      \"dist_to_left_boundary\": \"3333\",\"dist_to_right_boundary\": \"3333\",\"lane_sequences\": \"3333\"}]}"

        data_dict = {}
        data_dict["data"] = data
        session = requests.session()
        session.keep_alive = False
        # print(data)
        result = session.put(url=upload_url, data=data_dict)
        print(result)
        print("upload done")

    def upload_object_info_inbatch(self):
        # service_end_point = "http://10.3.1.30:8000/api/"
        service_end_point = "http://dataserver.prediction.simulation.deeproute.ai/api/"
        upload_url = service_end_point + "object_info/upload/"

        data = "{\"trajectory\":[{\"bagId\": \" test_test_frame_info\",\"perception_object_id\": \"2222\",\"trajectory\": [{ \"timestamp\": \"2323232\",  \"perception_obj_type\": \"xxx\",\"x\": \"1111\",\"y\": \"2222\",\"z\": \"3333\",\"l\": \"333\",   \"w\": \"333\",\"h\": \"45\",\"theta\": \"1111\",\"v_x\": \"2222\",\"v_y\": \"3333\",\"a_x\": \"333\",\"a_y\": \"333\",\"is_still\": \"false\",\"lane_s\": \"1111\",\"lane_l\": \"2222\",      \"dist_to_left_boundary\": \"3333\",\"dist_to_right_boundary\": \"3333\",\"lane_sequences\": \"3333\"}, {\"timestamp\": \"2323232\",      \"perception_obj_type\": \"xxx\",\"x\": \"1111\",\"y\": \"2222\",\"z\": \"3333\",\"l\": \"333\",   \"w\": \"333\",\"h\": \"45\",\"theta\": \"1111\",\"v_x\": \"2222\",\"v_y\": \"3333\",\"a_x\": \"333\",\"a_y\": \"333\",\"is_still\": \"false\",\"lane_s\": \"1111\",\"lane_l\": \"2222\",      \"dist_to_left_boundary\": \"3333\",\"dist_to_right_boundary\": \"3333\",\"lane_sequences\": \"3333\"},{ \"timestamp\": \"2323232\",      \"perception_obj_type\": \"xxx\",\"x\": \"1111\",\"y\": \"2222\",\"z\": \"3333\",\"l\": \"333\",   \"w\": \"333\",\"h\": \"45\",\"theta\": \"1111\",\"v_x\": \"2222\",\"v_y\": \"3333\",\"a_x\": \"333\",\"a_y\": \"333\",\"is_still\": \"false\",\"lane_s\": \"1111\",\"lane_l\": \"2222\",      \"dist_to_left_boundary\": \"3333\",\"dist_to_right_boundary\": \"3333\",\"lane_sequences\": \"3333\"}]},{\"bagId\": \" test_test_frame_info\",\"perception_object_id\": \"33333\",\"trajectory\": [{ \"timestamp\": \"2323232\",  \"perception_obj_type\": \"xxx\",\"x\": \"1111\",\"y\": \"2222\",\"z\": \"3333\",\"l\": \"333\",   \"w\": \"333\",\"h\": \"45\",\"theta\": \"1111\",\"v_x\": \"2222\",\"v_y\": \"3333\",\"a_x\": \"333\",\"a_y\": \"333\",\"is_still\": \"false\",\"lane_s\": \"1111\",\"lane_l\": \"2222\",      \"dist_to_left_boundary\": \"3333\",\"dist_to_right_boundary\": \"3333\",\"lane_sequences\": \"3333\"}, {\"timestamp\": \"2323232\",      \"perception_obj_type\": \"xxx\",\"x\": \"1111\",\"y\": \"2222\",\"z\": \"3333\",\"l\": \"333\",   \"w\": \"333\",\"h\": \"45\",\"theta\": \"1111\",\"v_x\": \"2222\",\"v_y\": \"3333\",\"a_x\": \"333\",\"a_y\": \"333\",\"is_still\": \"false\",\"lane_s\": \"1111\",\"lane_l\": \"2222\",      \"dist_to_left_boundary\": \"3333\",\"dist_to_right_boundary\": \"3333\",\"lane_sequences\": \"3333\"},{ \"timestamp\": \"2323232\",      \"perception_obj_type\": \"xxx\",\"x\": \"1111\",\"y\": \"2222\",\"z\": \"3333\",\"l\": \"333\",   \"w\": \"333\",\"h\": \"45\",\"theta\": \"1111\",\"v_x\": \"2222\",\"v_y\": \"3333\",\"a_x\": \"333\",\"a_y\": \"333\",\"is_still\": \"false\",\"lane_s\": \"1111\",\"lane_l\": \"2222\",      \"dist_to_left_boundary\": \"3333\",\"dist_to_right_boundary\": \"3333\",\"lane_sequences\": \"3333\"}]}]}"

        data_dict = {}
        data_dict["data"] = data
        session = requests.session()
        session.keep_alive = False
        # print(data)
        result = session.put(url=upload_url, data=data_dict)
        print(result)
        print("upload done")

    def upload_bag_info(self):
        # service_end_point = "http://127.0.0.1:8000/api/"
        # service_end_point = "http://10.3.1.30:8000/api/"
        service_end_point = "http://dataserver.prediction.simulation.deeproute.ai/api/"
        upload_url = service_end_point + "bag_info/upload/"

        data = "{\"bagId\": \" test_test_bag_info\",\"perception_object_ids\": \"{111, 222, 333, 444}\"}"
        data_dict = {}
        data_dict["data"] = data
        session = requests.session()
        session.keep_alive = False
        print(data)
        print("send out request")
        result = session.put(url=upload_url, data=data_dict)
        print(result)
        print("upload done")

    def upload_by_file(self):
        file_path = '/home/bruce/datahub/bag_'

        for iroot, idirs, ifiles in os.walk(file_path):
            for f in ifiles:
                filename = os.path.join(iroot, f)
                print(filename)
                self.upload_trajectory(filename)
                print("parse done!")

        # filename = '/home/bruce/datahub/data_hub/app/views/predictionData.txt'
        # upload_trajectory(filename)

    def test_mongo(self):
        host = '43.130.65.243'
        port = 37017
        authSource = "tw"
        print("connecting db")
        self.my_mongo_client = MongoClient(
            "mongodb://%s:%s@%s:%s/%s" % ('sky',
                                          'twitter', host, port, 'tw')
        )
        self.mongo_db = self.my_mongo_client["tw"]
        print(
            "Successfully connected to Mongo"
        )

        db_users = self.mongo_db["users"]
        query_result = db_users.find({"tst": "test"})
        for x in query_result:
            print(x)

    def test_consistency_check(self):
        service_end_point = "http://127.0.0.1:8000/api/consistency_test/YR_MKZ_1_20201207_022851_755_40/"
        session = requests.session()
        session.keep_alive = False
        print("sent out session")
        result = session.put(url=service_end_point)
        print("sent done")

    def upload_labeling_pose(self):
        print("into uploading pose")
        service_end_point = "http://127.0.0.1:8000/api/"
        # service_end_point = "http://dataserver.prediction.simulation.deeproute.ai/api/"
        upload_url = service_end_point + "labeling/pose/upload/"

        data_dict = dict()
        labeling_pose = list()
        for i in range(10):
            labeling_pose.append(i)
        data_dict["bagId"] = "YR_MKZ_1_20210105_biandao_PM2"
        data_dict["pose"] = str(labeling_pose)
        print(data_dict)
        session = requests.session()
        session.keep_alive = False
        result = session.put(url=upload_url, data=data_dict)
        print(result)

    def download_labeling_pose(self):
        print("into downloading pose")
        bagid = "YR_MKZ_1_20210105_biandao_PM2"
        service_end_point = "http://127.0.0.1:8000/api/"
        # service_end_point = "http://dataserver.prediction.simulation.deeproute.ai/api/"
        download_url = service_end_point + "labeling/pose/download/"

        data_dict = dict()
        data_dict["bagId"] = "YR_MKZ_1_20210105_biandao_PM2"

        print("send out request")
        session = requests.session()
        session.keep_alive = False
        result = session.put(url=download_url, data=data_dict)
        print(result.text)


if __name__ == '__main__':
    test = Test_UPload()
    # test.upload_attributes()
    # test.upload_attributes()
    # test.download_trajectory_data()
    # test.upload_object_info_inbatch()
    test.download_labeling_pose()
    # test.upload_trajectory_by_dict()
    # test.download_labeling_data()
    # test.test_mongo()
    print("try to get")
    # body = requests.get("http://www.baidu.com")
    # print(body)
