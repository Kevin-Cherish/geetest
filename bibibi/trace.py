import random
import pickle
import re

def get_trace_fast(distance):
    track = [[-random.randint(15, 22), -random.randint(22, 25), 0]]
    track.append([0, 0, 0])
    rand_x = 0
    passtime = 40
    for i in range(10):
        rand_x += int(distance * random.randint(1, 2) / 10)
        passtime += random.randint(10, 50)
        if rand_x < distance:
            track.append([rand_x, random.randint(-2, 2), passtime])
    passtime += random.randint(100, 150)
    track.append([distance,  random.randint(-2, 2), passtime])
    return track


def get_trace_normal(distance):
    track = [[random.randint(19, 30), random.randint(20, 25), 0]]
    count = 0
    scale = [0.2, 0.5, random.randint(6, 8) / 10]
    while count < distance:
        if count < distance * scale[0]:
            x = random.randint(1, 2)
        elif count < distance * scale[1]:
            x = random.randint(3, 4)
        elif count < distance * scale[2]:
            x = random.randint(5, 6)
        elif count < distance * 0.9:
            x = random.randint(2, 3)
        elif count < distance:
            x = 1
        count += x
        track.append([
            x,
            random.choice([0, 0, 0, 0, 0, 0, -1, 1]),
            random.randint(10, 20)
        ])

    track.append([0, 0, random.randint(300, 400)])
    return track


# 得到原始轨迹 [[x,y,t],...]
def format_track(track):
    track = re.findall('{(.*?)}', track)
    track_list = []
    for x in track:
        track_list.append([int(_) for _ in  x.split(',')])
    return track_list

def choice_track_list(dist):
    source_track = [
        '{-13,-23,0};{0,0,0};{1,0,91};{2,0,96};{5,0,107};{9,0,112};{12,0,121};{15,0,128};{17,0,137};{20,0,144};{23,0,152};{26,0,160};{29,0,168};{32,0,176};{35,0,184};{39,0,192};{44,0,200};{51,0,208};{58,0,216};{64,0,224};{69,0,232};{73,0,240};{78,0,248};{82,0,256};{86,0,264};{90,0,272};{99,0,280};{105,0,288};{114,0,296};{121,0,304};{126,0,312};{132,0,320};{137,0,328};{141,0,336};{146,0,344};{149,0,353};{151,0,360};{154,0,368};{156,0,376};{157,0,385};{158,0,392};{160,0,401};{161,0,408};{162,0,432};{163,0,440};{164,1,448};{166,1,464};{168,1,472};{169,1,480};{170,1,488};{171,1,496};{172,1,504};{173,1,512};{174,1,519};{175,1,528};{176,1,536};{177,1,544};{179,1,552};{180,1,568};{181,1,584};{182,1,600};{183,1,608};{184,1,623};{185,1,632};{186,1,640};{188,1,655};{189,1,664};{191,1,681};{192,1,728};{194,1,760};{194,1,1127};{194,1,1127};{194,1,1127};{194,1,1128};{192,1,1479};{190,1,1511};{189,1,1536};{189,1,1841};',
        '{-18,-19,0};{0,0,0};{2,0,256};{4,-1,266};{6,-1,272};{8,-3,282};{9,-3,297};{11,-3,313};{12,-3,360};{13,-4,376};{14,-4,433};{15,-4,449};{16,-4,456};{18,-4,473};{19,-4,520};{19,-4,542};{19,-4,543};{19,-4,543};{19,-4,544};{20,-4,546};{20,-4,549};{20,-4,549};{20,-4,549};{20,-4,550};{20,-4,550};{20,-4,552};{20,-4,552};{20,-4,553};{20,-4,554};{21,-4,585};{22,-4,633};{24,-4,657};{24,-4,678};{24,-4,678};{24,-4,678};{25,-4,728};{27,-4,777};{28,-4,809};{29,-4,858};{30,-4,880};{31,-4,889};{32,-4,920};{33,-4,936};{34,-4,960};{35,-4,984};{36,-4,992};{37,-4,1016};{38,-4,1056};{39,-4,1089};{40,-4,1144};{41,-4,1176};{42,-4,1203};{43,-4,1219};{44,-4,1241};{46,-4,1250};{48,-4,1283};{49,-4,1329};{51,-4,1377};{52,-4,1441};{54,-4,1504};{55,-4,1530};{56,-4,1536};{57,-4,1547};{58,-4,1553};{60,-4,1577};{61,-4,1594};{63,-4,1649};{64,-4,1672};{66,-4,1704};{67,-3,1754};{68,-3,1906};{69,-3,1912};{71,-3,1928};{72,-3,1945};{73,-3,1960};{74,-3,1977};{75,-3,1993};{75,-2,2001};{76,-2,2064};{77,-2,2072};{78,-2,2089};{79,-2,2233};{80,-2,2408};{81,-2,2416};{82,-2,2450};{83,-2,2504};{84,-2,2552};{85,-2,2640};{86,-2,2664};{88,-1,2697};{89,-1,2768};{90,-1,2785};{91,-1,3120};{92,-1,3168};{94,0,3184};{95,0,3224};{96,0,3249};{97,0,3280};{97,1,3304};{98,1,3369};{99,1,3401};{100,1,3448};{101,1,3546};{102,1,3601};{103,1,3656};{104,1,3794};{106,1,3809};{107,1,3825};{108,1,3842};{109,1,3928};{110,1,3976};{111,1,4000};{112,2,4096};{113,2,4224};{114,2,4240};{115,2,4276};{116,3,4296};{117,3,4338};{118,3,4354};{119,3,4392};{120,3,4409};{121,3,4417};{121,4,4424};{122,4,4457};{123,4,4472};{124,4,4512};{125,4,4584};{126,4,4634};{127,4,4656};{128,4,4704};{129,4,4713};{130,4,4728};{131,4,4760};{132,4,4777};{133,4,4784};{134,5,4792};{135,5,4801};{136,5,4809};{138,6,4840};{139,6,4864};{140,6,4888};{141,6,4899};{142,6,4912};{143,6,4946};{144,6,4961};{145,6,4968};{146,6,4994};{147,6,5010};{148,6,5032};{149,6,5080};{150,6,5121};{151,6,5136};{152,6,5241};{153,6,5305};{155,7,5328};{156,7,5489};{157,7,5544};{158,7,5624};{159,7,5632};{160,7,5696};{162,8,5800};{162,9,5824};{163,9,5856};{164,9,5897};{165,9,5912};{166,9,5954};{167,9,5955};{168,9,5968};{169,9,6032};{170,9,6072};{171,9,6108};{172,9,6128};{173,9,6225};{174,9,6256};{175,9,6272};{176,9,6368};{177,9,6416};{178,9,6456};{179,9,6560};{181,10,6600};{182,10,6696};{183,10,6744};{184,10,6760};{185,10,6888};{186,10,6936};{187,10,6976};{188,10,7096};{189,10,7104};{190,10,7129};{191,10,7177};{192,10,7193};{193,10,7200};{194,10,7248};{195,10,7264};{196,10,7280};{198,11,7320};{198,12,7344};{199,12,7352};{200,12,7448};{201,12,7512};{202,12,7521};{203,12,7664};{204,12,7680};{205,12,7720};{206,12,7786};{207,12,7824};{208,13,7840};{209,13,8008};{209,13,8042};',
        '{-25,-20,0};{0,0,0};{-1,0,63};{-1,-1,79};{-1,-3,95};{0,-3,103};{0,-3,106};{0,-3,107};{0,-3,107};{0,-3,107};{0,-3,108};{0,-3,108};{0,-3,109};{0,-3,109};{0,-3,109};{1,-3,110};{2,-3,119};{5,-3,127};{8,-3,135};{9,-4,143};{12,-4,151};{15,-4,159};{19,-4,167};{23,-4,175};{28,-4,183};{33,-4,191};{37,-4,199};{42,-4,207};{49,-4,215};{57,-4,223};{62,-4,231};{71,-4,241};{77,-4,248};{77,-4,249};{77,-4,249};{77,-4,249};{86,-4,256};{91,-4,263};{95,-4,272};{100,-4,279};{103,-4,289};{107,-4,295};{111,-4,303};{115,-4,311};{118,-4,319};{120,-4,327};{124,-4,335};{127,-4,343};{128,-4,351};{130,-4,359};{132,-4,367};{134,-4,375};{137,-4,383};{139,-4,391};{140,-4,399};{141,-4,407};{142,-4,423};{143,-4,431};{144,-4,447};{145,-4,455};{146,-4,463};{148,-4,471};{150,-4,487};{151,-4,495};{154,-4,503};{157,-4,512};{158,-4,519};{160,-4,527};{162,-4,535};{164,-4,543};{165,-4,551};{166,-4,559};{167,-4,567};{168,-4,575};{169,-4,591};{170,-4,607};{171,-4,623};{172,-4,640};{174,-4,647};{175,-4,663};{176,-4,671};{177,-4,687};{178,-4,759};{179,-4,767};{180,-4,783};{181,-4,847};{182,-4,863};{183,-4,871};{184,-4,975};{185,-4,991};{186,-4,1056};{187,-4,1074};{188,-4,1079};{189,-4,1096};{189,-4,1463};',
        '{-23,-18,0};{0,0,0};{0,0,0};{0,1,285};{1,1,293};{3,1,309};{5,1,317};{8,1,325};{11,1,336};{14,1,341};{15,1,351};{17,1,357};{19,1,366};{21,1,373};{22,1,382};{24,1,389};{26,1,398};{29,1,405};{32,1,414};{33,1,421};{36,1,429};{39,1,437};{40,1,445};{43,1,453};{44,1,461};{46,1,469};{47,1,477};{50,1,486};{51,1,501};{54,1,509};{55,1,518};{57,1,525};{58,1,534};{61,2,541};{62,2,550};{64,2,557};{66,2,566};{68,2,573};{69,2,589};{70,2,597};{72,2,605};{73,2,621};{74,2,630};{75,2,637};{76,2,653};{77,2,662};{78,2,669};{79,2,686};{80,2,695};{81,2,701};{82,2,717};{84,2,725};{86,2,741};{87,2,749};{88,2,765};{89,2,781};{91,2,814};{92,2,821};{93,2,829};{94,2,837};{96,2,845};{97,2,853};{99,2,862};{100,2,869};{101,2,878};{102,2,886};{103,2,901};{104,2,909};{105,2,917};{107,2,943};{108,2,949};{109,2,957};{110,2,965};{111,2,973};{112,2,981};{115,2,990};{116,2,1007};{118,2,1014};{120,2,1029};{121,2,1039};{123,2,1054};{124,2,1061};{125,2,1070};{126,2,1086};{128,2,1094};{130,2,1109};{132,1,1117};{134,1,1150};{135,1,1205};{137,1,1229};{138,1,1253};{139,1,1285};{140,1,1325};{140,1,1598};',
        '{-11,-25,0};{0,0,0};{0,0,5};{3,1,229};{6,1,237};{8,1,245};{10,2,253};{11,2,262};{12,2,269};{13,2,278};{14,2,293};{16,2,333};{17,2,342};{18,2,373};{19,2,381};{20,2,389};{21,2,397};{22,2,406};{23,2,413};{24,2,421};{26,2,429};{27,2,437};{29,2,453};{30,2,477};{32,2,485};{33,2,493};{34,2,501};{35,2,509};{36,2,517};{38,2,525};{39,2,541};{40,2,558};{41,2,573};{42,2,581};{43,2,589};{45,2,597};{46,2,605};{48,2,613};{49,2,621};{52,2,629};{53,2,637};{56,2,645};{57,2,654};{59,2,661};{62,2,669};{67,2,677};{70,2,685};{73,2,693};{76,2,701};{78,2,709};{79,2,717};{81,2,725};{83,2,733};{85,2,749};{86,2,765};{88,2,773};{89,2,781};{90,2,789};{91,2,797};{92,2,813};{93,2,821};{94,2,829};{96,2,845};{96,3,854};{97,3,861};{98,3,877};{99,3,893};{100,3,902};{101,3,958};{102,3,1017};{103,3,1038};{104,3,1181};{105,3,1205};{107,4,1248};{108,4,1365};{109,4,1381};{110,4,1638};{110,4,1825};',
        '{-16,-23,0};{0,0,0};{1,0,232};{5,0,240};{7,0,248};{9,0,255};{10,0,264};{12,0,272};{14,1,280};{15,1,288};{17,1,296};{18,1,304};{19,2,320};{21,2,328};{22,2,336};{24,3,345};{26,3,352};{29,3,360};{32,3,368};{34,3,376};{37,3,384};{40,3,393};{45,5,400};{49,5,408};{55,6,416};{63,6,423};{67,6,432};{73,6,440};{78,6,448};{82,6,456};{85,6,464};{88,6,472};{89,6,488};{92,6,495};{96,6,504};{99,6,512};{100,6,528};{102,6,600};{103,6,624};{106,6,632};{110,7,642};{114,7,648};{118,7,658};{122,7,664};{128,7,674};{135,7,680};{142,7,689};{146,7,696};{150,7,705};{153,7,712};{155,7,720};{158,7,727};{161,7,736};{164,7,744};{166,7,752};{168,7,759};{169,7,768};{172,7,775};{174,7,784};{176,7,792};{177,7,895};{176,7,1104};{173,7,1118};{171,7,1131};{170,7,1149};{169,7,1641};{168,7,1657};{167,7,1704};{167,7,2144};',
        '{-10,-20,0};{0,0,0};{1,0,164};{2,0,212};{3,0,228};{4,0,244};{5,0,270};{6,0,277};{7,0,292};{8,0,309};{9,0,318};{10,0,324};{11,0,340};{12,0,356};{13,0,365};{14,0,388};{15,0,396};{16,0,404};{17,0,420};{18,0,429};{19,0,436};{20,0,468};{21,0,492};{22,0,524};{24,0,534};{25,0,550};{26,0,566};{27,0,572};{28,0,583};{30,0,597};{31,0,613};{33,0,630};{35,0,636};{36,0,646};{37,0,652};{39,0,661};{41,0,668};{43,0,677};{44,0,684};{45,0,692};{47,0,701};{48,0,716};{50,0,726};{51,0,748};{52,1,764};{53,1,780};{54,1,812};{55,1,820};{56,1,828};{57,1,845};{58,1,852};{59,1,861};{60,1,878};{61,1,884};{62,1,893};{63,1,900};{64,1,908};{65,1,916};{66,1,932};{68,1,941};{69,1,948};{70,2,964};{71,2,972};{72,2,980};{74,2,988};{75,2,1004};{77,2,1021};{78,2,1037};{80,2,1052};{80,3,1060};{81,3,1076};{83,3,1141};{84,3,1334};{86,3,1356};{87,3,1437};{87,2,1542};{86,2,1566};{84,1,1572};{83,1,1588};{81,1,1605};{80,1,1621};{79,1,1636};{78,1,1644};{77,1,1669};{76,0,1700};{76,0,2158};',
        '{-27,-20,0};{0,0,0};{1,0,175};{2,0,183};{5,0,191};{6,0,200};{8,0,215};{9,0,225};{10,0,232};{11,0,240};{12,0,263};{13,0,273};{15,0,279};{17,0,295};{18,0,304};{21,0,312};{22,0,320};{24,0,328};{26,0,336};{28,0,343};{30,0,352};{33,0,359};{36,0,369};{39,0,375};{41,0,383};{44,0,391};{47,0,399};{49,0,407};{52,0,415};{54,0,423};{55,0,431};{58,0,439};{60,0,447};{63,0,456};{66,0,464};{69,0,471};{70,0,479};{73,0,487};{74,0,495};{76,0,504};{77,0,523};{79,0,527};{81,0,543};{84,0,553};{85,0,559};{86,0,570};{87,0,576};{89,0,589};{90,0,593};{92,0,601};{93,0,608};{95,0,624};{97,0,633};{99,1,640};{100,1,648};{101,1,656};{103,1,666};{104,2,672};{106,2,688};{107,2,696};{108,2,704};{109,2,713};{110,2,728};{111,2,736};{113,2,744};{114,2,760};{116,2,771};{117,2,776};{118,2,784};{120,3,792};{120,4,802};{121,4,816};{122,4,824};{123,4,834};{125,4,840};{126,4,856};{128,4,866};{129,4,880};{131,4,904};{132,4,936};{133,4,944};{134,4,960};{135,4,976};{136,4,984};{137,4,992};{139,4,1008};{140,4,1016};{141,4,1024};{142,4,1032};{143,4,1040};{144,4,1048};{145,4,1064};{146,4,1072};{147,4,1080};{148,4,1113};{149,4,1121};{150,4,1152};{151,4,1688};{152,4,1818};{152,4,2331};'
    ]
    # return source_track

    # linux 和widow不同 # 从dos转为Unix
    # original = "t_dict_unix.pkl"
    # destination = "t_dict.pkl"
    #
    # content = ''
    # outsize = 0
    # with open(original, 'rb') as infile:
    #     content = infile.read()
    # with open(destination, 'wb') as output:
    #     for line in content.splitlines():
    #         outsize += len(line) + 1
    #         output.write(line + str.encode('\n'))

    t_dict = pickle.load(open('t_dict.pkl', 'rb'))

    if str(dist) in t_dict:
        print('in file %s' % dist)
        return t_dict[str(dist)], 1
    if str(dist - 1) in t_dict:
        print('in file %s-1' % (dist))
        return t_dict[str(dist - 1)], 1
    if str(dist + 1) in t_dict:
        print('in file %s+1' % (dist))
        return t_dict[str(dist + 1)], 1
    if str(dist - 2) in t_dict:
        print('in file %s-2' % (dist))
        return t_dict[str(dist - 2)], 1
    if str(dist + 2) in t_dict:
        print('in file %s+2' % (dist))
        return t_dict[str(dist + 2)], 1

    # 先前没有保存t_dict.pkl的时候 使用了source_track中的值
    # 若t_dick收集的完善，将不会执行到这一步，可将一下代码注释
    # 若某个小概率距离t_dick中未出现，则从source_track的轨迹中截取
    s = '{%d,' % dist
    print(s)
    tmp_track_list = []
    for item in source_track[:]:
        if s in item:
            tmp_track_list.append(item)
    if len(tmp_track_list) > 0:
        return random.sample(tmp_track_list, 1)[0], 0
    else:
        return source_track[0], 0

def choice_track(dist):
    track, tag = choice_track_list(dist)  # 来自训练路径 tag=1
    # 规范化轨迹数据  [[x,y,t],...]
    track_list = format_track(track)  # 路径列表
    # 若tag==0,即轨迹数据不在已收集的轨迹文件中（来自候选轨迹列表）,
    # 则截取路径（从中截取需要的长度）
    if tag != 1:
        # 采用垃圾算法获取轨迹 建议重写
        new_track_list = get_trace_fast(dist)
    else:
        # tag==1 轨迹数据来自文件 直接赋值
        new_track_list = track_list
    return new_track_list

if __name__ == '__main__':
    print(choice_track(76))