import requests
import random
from io import BytesIO
from PIL import Image

BASE_URL = 'https://storage.googleapis.com/onlinehack-monkeys/'

MONKEYS = [
# chimpanzees
*'''110019698_1457d6ea36.jpg
1161792822_02c09fd798.jpg
1212980669_e3a2e94897.jpg
1319804437_ba45ded6d9.jpg
1521537828_a38a2be400.jpg
153043237_c4f2b2bc91.jpg
1613583204_cd61cd98f4.jpg
164229506_12a09cb99a.jpg
165050888_dcb47363be.jpg
165158073_15e0e1a808.jpg
2020310747_18c6aa1499.jpg
2020369737_f9be0d0ee0.jpg
2021168238_b52cb6af60.jpg
2032118442_98e0ff4b29.jpg
2078349826_7ac4cd0e9f.jpg
2113760232_f0a119623c.jpg
213359054_c1732a73d1.jpg
2175116127_81841e0783.jpg
278050476_cbb4865c2c.jpg
293584618_571a7e0580.jpg
330006818_17f67e6d2b.jpg
373298584_77c44efc85.jpg
391127442_fa5a132e33.jpg
450431844_658e771446.jpg
456748651_e19c947326.jpg
459276648_36649b3f9d.jpg
47863396_49b5d88e49.jpg
598330495_33b4caa842.jpg
606903188_7471556f7a.jpg
784726387_161c96e6ef.jpg
785603342_eb0d3a5bca.jpg
906049226_da2aa23a80.jpg
906064372_22cc3559d1.jpg
975710373_51da77ecbf.jpg
AW_Chimp20.jpg
chimpanzee52.jpg'''.split('\n'),
# gorillas
*'''108798145_1c7df20326.jpg
129288719_15ae3337f0.jpg
1505359832_302891fc77.jpg
1517537894_9d838c175c.jpg
1574617236_e78ab3c752.jpg
1576247444_db8de6af44.jpg
1906228711_1fc5301bd6.jpg
2048768438_d6be4c6803.jpg
211168870_4a74f08223.jpg
2165789809_b89eae481b.jpg
2166586256_a602525671.jpg
226142309_b03e4b1813.jpg
261368936_7b17c92d5d.jpg
405814212_8b965ff0be.jpg
418522015_e30601ed44.jpg
425624593_5eb2f08952.jpg
446253329_6ad1f40f28.jpg
450658866_b86e29129b.jpg
485343209_8bc612ac7a.jpg
497290038_612abf9d63.jpg
499183183_e8b79f7982.jpg
516804820_e0add1b731.jpg
570171470_6619bf60c7.jpg
690050192_d59905b9d4.jpg
85532291_7794a85dca.jpg
89590500_030b4004e4.jpg
gabon_1589.JPG'''.split('\n'),
# orangutangs
*'''1026681594_e0b67ed0bd.jpg
1101185967_bb8fb2bcc1.jpg
124790257_1a701674a2.jpg
1337174989_bd6bb4206c.jpg
135748860_c886febd9d.jpg
1484466108_417362baae.jpg
1492076846_46a77a3edf.jpg
190088459_336974bf43.jpg
20060428204847-orangutan-baby.jpg
200859491_5b793ab38e.jpg
2175544803_58164f6d23.jpg
257847866_82b845cf2a.jpg
297118456_100cf839fb.jpg
312869762_31307cba44.jpg
329645997_43cefc9d54.jpg
337342930_290c3fb45d.jpg
347601023_24e761ae10.jpg
364185879_94c0d9a48f.jpg
387252542_82eabb41b0.jpg
407832585_33941a693a.jpg
414042761_4594bac44f.jpg
415657936_2e833144f4.jpg
437599197_3e795642bc.jpg
45405459_c833ad3cc1.jpg
504093966_4830f4037c.jpg
693047864_fc1f617611.jpg
814300210_6f424271fe.jpg
814301244_07e12f7f33.jpg
917699137_45a71f9a7f.jpg'''.split('\n'),
]


def get_monkey():
    url = BASE_URL + MONKEYS[random.randint(0, len(MONKEYS) - 1)]
    print(url)
    res = requests.get(url)
    file = BytesIO()
    file.write(res.content)
    file.seek(0)
    image = Image.open(file)
    return image
