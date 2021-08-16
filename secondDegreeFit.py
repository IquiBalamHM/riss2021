# fit a straight line to the economic data
from re import X
from Fits import * 



    
# load the dataset
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/longley.csv'
dataframe = read_csv(url, header=None)
data = dataframe.values
# choose the input and output variables
#x, y = data[:, 4], data[:, -1]
# curve fit
x = [-230.0, -217.0, -203.0, -186.0, -168.0, -150.0, -133.0, -118.0, -103.0, -85.0, -65.0, -46.0, -37.0, -36.0, -20.0, 0.0, 19.0, 36.0, 41.0, 44.0, 63.0, 81.0, 100.0, 117.0, 124.0, 136.0, 149.0, 168.0, 186.0, 191.0, 209.0]
y = [169.0, 154.0, 140.0, 130.0, 121.0, 111.0, 100.0, 87.0, 74.0, 65.0, 60.0, 54.0, 36.0, 16.0, 4.0, 0.0, -5.0, -16.0, -35.0, -55.0, -62.0, -70.0, -76.0, -88.0, -107.0, -123.0, -138.0, -144.0, -152.0, -172.0, -181.0]
x = [20, 36, 53, 71, 89, 108, 128, 148, 168, 187, 206, 224, 242, 260, 279, 301, 322, 345, 369, 394, 419, 442, 465, 487, 509, 529, 550, 569, 588, 605, 620]
y = [240, 253, 268, 281, 293, 302, 310, 317, 324, 331, 340, 348, 357, 365, 372, 377, 370, 375, 378, 377, 372, 365, 355, 343, 331, 318, 304, 289, 273, 255, 240]

x=[48, 68, 90, 112, 134, 156, 176, 195, 213, 230, 246, 262, 277, 291, 306, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620]
y=[438, 431, 424, 417, 411, 402, 391, 378, 363, 346, 329, 311, 293, 275, 256, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240, 240]
x = [0,1/4,1/2,3/4,1]
y = [1/2,1/4,0,-1/4,-1/2]


x=[-300.0, -278.74161972158754, -256.72792236706823, -234.65624838291637, -211.62773234756844, -188.03827420772083, -164.66757891218361, -141.7877985227594, -119.55691906677339, -97.9590886426289, -76.85323244306656, -56.17697556910974, -35.715334578099885, -15.2169536763314, 5.135839970158543, 24.932204892921504, 44.29235212912823, 63.77620176066176, 83.65310324203813, 103.81408392077765, 124.17071263815939, 145.02287839435132, 166.07755398127205, 186.33484476013336, 205.62377039068508, 223.6833442756107, 238.088025049341, 253.46883598052193, 269.5840472027071, 286.0057047913715, 300.0]
y=[0.0, 7.18667665633842, 15.516956069864165, 23.292867426398686, 27.46557268630707, 26.29261933043358, 21.240240104333196, 13.53808954733816, 3.862661121672147, -7.063065165318562, -18.548632419922967, -30.218627496718966, -41.56241580982436, -52.15345877165231, -62.47517649610376, -73.43086863384048, -84.79801961703475, -95.58984370794502, -105.24850012111187, -113.76246875372493, -121.15768597656347, -126.63921308443895, -128.00905300401763, -123.1994468073272, -111.35517646183644, -95.84478227831107, -77.03082053592829, -57.063323202676145, -36.93909824430119, -16.932204285178955, 0.0]
x2=[-300, -299, -298, -297, -296, -295, -294, -293, -292, -291, -290, -289, -288, -287, -286, -285, -284, -283, -282, -281, -280, -279, -278, -277, -276, -275, -274, -273, -272, -271, -270, -269, -268, -267, -266, -265, -264, -263, -262, -261, -260, -259, -258, -257, -256, -255, -254, -253, -252, -251, -250, -249, -248, -247, -246, -245, -244, -243, -242, -241, -240, -239, -238, -237, -236, -235, -234, -233, -232, -231, -230, -229, -228, -227, -226, -225, -224, -223, -222, -221, -220, -219, -218, -217, -216, -215, -214, -213, -212, -211, -210, -209, -208, -207, -206, -205, -204, -203, -202, -201, -200, -199, -198, -197, -196, -195, -194, -193, -192, -191, -190, -189, -188, -187, -186, -185, -184, -183, -182, -181, -180, -179, -178, -177, -176, -175, -174, -173, -172, -171, -170, -169, -168, -167, -166, -165, -164, -163, -162, -161, -160, -159, -158, -157, -156, -155, -154, -153, -152, -151, -150, -149, -148, -147, -146, -145, -144, -143, -142, -141, -140, -139, -138, -137, -136, -135, -134, -133, -132, -131, -130, -129, -128, -127, -126, -125, -124, -123, -122, -121, -120, -119, -118, -117, -116, -115, -114, -113, -112, -111, -110, -109, -108, -107, -106, -105, -104, -103, -102, -101, -100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299]
y2=[61, 60, 60, 59, 58, 58, 57, 56, 56, 55, 54, 54, 53, 52, 52, 51, 51, 50, 49, 49, 48, 47, 47, 46, 46, 45, 44, 44, 43, 42, 42, 41, 41, 40, 39, 39, 38, 38, 37, 36, 36, 35, 35, 34, 33, 33, 32, 32, 31, 31, 30, 29, 29, 28, 28, 27, 26, 26, 25, 25, 24, 24, 23, 23, 22, 21, 21, 20, 20, 19, 19, 18, 18, 17, 16, 16, 15, 15, 14, 14, 13, 13, 12, 12, 11, 10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0, 0, 0, 0, -1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7, -7, -8, -8, -8, -9, -9, -10, -10, -11, -11, -12, -12, -13, -13, -14, -14, -14, -15, -15, -16, -16, -17, -17, -18, -18, -18, -19, -19, -20, -20, -21, -21, -21, -22, -22, -23, -23, -24, -24, -24, -25, -25, -26, -26, -26, -27, -27, -28, -28, -28, -29, -29, -30, -30, -30, -31, -31, -32, -32, -32, -33, -33, -33, -34, -34, -35, -35, -35, -36, -36, -36, -37, -37, -38, -38, -38, -39, -39, -39, -40, -40, -40, -41, -41, -41, -42, -42, -43, -43, -43, -44, -44, -44, -45, -45, -45, -46, -46, -46, -47, -47, -47, -47, -48, -48, -48, -49, -49, -49, -50, -50, -50, -51, -51, -51, -52, -52, -52, -52, -53, -53, -53, -54, -54, -54, -54, -55, -55, -55, -56, -56, -56, -56, -57, -57, -57, -57, -58, -58, -58, -59, -59, -59, -59, -60, -60, -60, -60, -61, -61, -61, -61, -62, -62, -62, -62, -63, -63, -63, -63, -63, -64, -64, -64, -64, -65, -65, -65, -65, -66, -66, -66, -66, -66, -67, -67, -67, -67, -67, -68, -68, -68, -68, -68, -69, -69, -69, -69, -69, -70, -70, -70, -70, -70, -71, -71, -71, -71, -71, -71, -72, -72, -72, -72, -72, -72, -73, -73, -73, -73, -73, -73, -74, -74, -74, -74, -74, -74, -74, -75, -75, -75, -75, -75, -75, -75, -76, -76, -76, -76, -76, -76, -76, -76, -77, -77, -77, -77, -77, -77, -77, -77, -77, -78, -78, -78, -78, -78, -78, -78, -78, -78, -78, -79, -79, -79, -79, -79, -79, -79, -79, -79, -79, -79, -79, -80, -80, -80, -80, -80, -80, -80, -80, -80, -80, -80, -80, -80, -80, -80, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -81, -80, -80, -80, -80, -80, -80, -80, -80, -80, -80, -80, -80, -80, -80, -80, -80, -79, -79, -79, -79, -79, -79, -79, -79, -79, -79, -79, -79, -78, -78, -78, -78, -78, -78, -78, -78, -78, -77, -77, -77, -77, -77, -77, -77, -77, -77, -76, -76, -76, -76, -76, -76, -76, -76, -75, -75, -75, -75, -75, -75, -75, -74, -74, -74, -74, -74, -74, -74, -73, -73, -73, -73, -73, -73, -72, -72, -72, -72, -72, -72, -71, -71, -71, -71, -71, -71, -70, -70, -70, -70, -70, -69, -69, -69, -69, -69, -68, -68, -68, -68, -68, -67, -67, -67, -67, -67, -66, -66, -66, -66, -66, -65, -65, -65, -65, -64, -64, -64, -64, -64, -63, -63, -63, -63, -62, -62, -62, -62, -61]
for i in range(len(x)):
#    x[i] += 320
    y[i] = (y[i]-240)*-1
for i in range(len(x2)):
    y2[i] = (y2[i]-240)*-1
#print(x)
x=[-300.0, -278.6413469901951, -256.339911767663, -234.03702704167006, -211.83467929997943, -189.8464649490613, -168.2209773463005, -147.14156039075618, -126.70994075850473, -106.84979472245271, -87.43297595459202, -68.54543809002749, -50.38628091227292, -32.79234565487536, -15.380267340456442, 1.9267093204933303, 19.11260780824807, 36.33831315182698, 54.09627619086763, 74.72714123159466, 99.17065173612696, 124.83956157969158, 150.60871599338174, 175.58509597354032, 194.79875236646683, 209.70106127417466, 224.6594899948251, 240.71226960869888, 259.07412004796413, 279.9235002722188, 300.0]
y=[0.0, 4.347717631096742, 8.117531569124935, 10.853791017564674, 12.421054971990856, 12.610299995431347, 11.131395290035869, 7.852835178588663, 2.972501333440391, -3.141645656739996, -10.342660133149451, -18.98851052581938, -29.362301047019912, -40.96233909488052, -52.98384774127874, -65.00035455220797, -76.80865008391112, -88.4389703014989, -100.21355020948329, -109.6101793761847, -111.92709049056924, -114.27165958944767, -107.03194829050341, -101.26980923845025, -86.36949485344769, -66.66676845900639, -47.51559461243721, -30.124326135633453, -15.914366141959533, -6.145601019596967, 0.0]
x2=[-300, -299, -298, -297, -296, -295, -294, -293, -292, -291, -290, -289, -288, -287, -286, -285, -284, -283, -282, -281, -280, -279, -278, -277, -276, -275, -274, -273, -272, -271, -270, -269, -268, -267, -266, -265, -264, -263, -262, -261, -260, -259, -258, -257, -256, -255, -254, -253, -252, -251, -250, -249, -248, -247, -246, -245, -244, -243, -242, -241, -240, -239, -238, -237, -236, -235, -234, -233, -232, -231, -230, -229, -228, -227, -226, -225, -224, -223, -222, -221, -220, -219, -218, -217, -216, -215, -214, -213, -212, -211, -210, -209, -208, -207, -206, -205, -204, -203, -202, -201, -200, -199, -198, -197, -196, -195, -194, -193, -192, -191, -190, -189, -188, -187, -186, -185, -184, -183, -182, -181, -180, -179, -178, -177, -176, -175, -174, -173, -172, -171, -170, -169, -168, -167, -166, -165, -164, -163, -162, -161, -160, -159, -158, -157, -156, -155, -154, -153, -152, -151, -150, -149, -148, -147, -146, -145, -144, -143, -142, -141, -140, -139, -138, -137, -136, -135, -134, -133, -132, -131, -130, -129, -128, -127, -126, -125, -124, -123, -122, -121, -120, -119, -118, -117, -116, -115, -114, -113, -112, -111, -110, -109, -108, -107, -106, -105, -104, -103, -102, -101, -100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299]
y2=[188, 189, 190, 190, 191, 191, 192, 193, 193, 194, 195, 195, 196, 196, 197, 198, 198, 199, 199, 200, 201, 201, 202, 202, 203, 204, 204, 205, 205, 206, 206, 207, 208, 208, 209, 209, 210, 211, 211, 212, 212, 213, 213, 214, 214, 215, 216, 216, 217, 217, 218, 218, 219, 219, 220, 221, 221, 222, 222, 223, 223, 224, 224, 225, 225, 226, 226, 227, 227, 228, 228, 229, 229, 230, 231, 231, 232, 232, 233, 233, 234, 234, 235, 235, 236, 236, 237, 237, 238, 238, 238, 239, 239, 240, 240, 240, 240, 241, 241, 242, 242, 243, 243, 244, 244, 245, 245, 245, 246, 246, 247, 247, 248, 248, 249, 249, 250, 250, 250, 251, 251, 252, 252, 253, 253, 253, 254, 254, 255, 255, 256, 256, 256, 257, 257, 258, 258, 258, 259, 259, 260, 260, 260, 261, 261, 262, 262, 262, 263, 263, 264, 264, 264, 265, 265, 266, 266, 266, 267, 267, 267, 268, 268, 269, 269, 269, 270, 270, 270, 271, 271, 271, 272, 272, 272, 273, 273, 273, 274, 274, 274, 275, 275, 275, 276, 276, 276, 277, 277, 277, 278, 278, 278, 279, 279, 279, 280, 280, 280, 281, 281, 281, 282, 282, 282, 282, 283, 283, 283, 284, 284, 284, 284, 285, 285, 285, 286, 286, 286, 286, 287, 287, 287, 288, 288, 288, 288, 289, 289, 289, 289, 290, 290, 290, 290, 291, 291, 291, 291, 292, 292, 292, 292, 293, 293, 293, 293, 294, 294, 294, 294, 294, 295, 295, 295, 295, 296, 296, 296, 296, 296, 297, 297, 297, 297, 297, 298, 298, 298, 298, 298, 299, 299, 299, 299, 299, 299, 300, 300, 300, 300, 300, 301, 301, 301, 301, 301, 301, 302, 302, 302, 302, 302, 302, 303, 303, 303, 303, 303, 303, 303, 304, 304, 304, 304, 304, 304, 304, 304, 305, 305, 305, 305, 305, 305, 305, 305, 306, 306, 306, 306, 306, 306, 306, 306, 306, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 308, 308, 308, 308, 308, 308, 308, 308, 308, 308, 308, 308, 308, 308, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 310, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 308, 308, 308, 308, 308, 308, 308, 308, 308, 308, 308, 308, 308, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 307, 306, 306, 306, 306, 306, 306, 306, 306, 306, 305, 305, 305, 305, 305, 305, 305, 305, 304, 304, 304, 304, 304, 304, 304, 303, 303, 303, 303, 303, 303, 303, 302, 302, 302, 302, 302, 302, 301, 301, 301, 301, 301, 301, 300, 300, 300, 300, 300, 300, 299, 299, 299, 299, 299, 298, 298, 298, 298, 298, 297, 297, 297, 297, 297, 296, 296, 296, 296, 296, 295, 295, 295, 295, 294, 294, 294, 294, 294, 293, 293, 293, 293, 292, 292, 292, 292, 291, 291, 291, 291, 290, 290, 290, 290, 289, 289, 289, 289, 288, 288, 288, 288, 287, 287, 287, 286, 286, 286, 286, 285, 285, 285, 285, 284, 284, 284, 283, 283, 283, 282, 282, 282, 282, 281, 281, 281, 280, 280, 280, 279, 279, 279, 278, 278, 278, 278, 277, 277, 277, 276, 276, 276, 275, 275, 275, 274, 274]
#tempfit = CurveFit(x,y,2)

# create a line plot for the mapping function
pyplot.plot(x, y, '-', color='blue')
pyplot.plot(x2, y2, '--', color='red')

pyplot.show()
