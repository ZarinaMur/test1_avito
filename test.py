from playwright.sync_api import Page, expect
import time
import json


def test_water(page: Page):

    a = [1, 999, 1000, 1001, 9954, 9955, 10000, 10001, 10049, 10050, 99950, 100000, 100499, 100500, 999449, 999500,
          1000000, 1044000, 1045000, 999449000, 999500000, 1000000000]
    for i, elem in enumerate(a):
        page.goto("https://www.avito.ru/avito-care/eco-impact", wait_until="domcontentloaded")

        def intercept(route):
            new_response = json.dumps({
                "result": {
                    "blocks": {
                        "personalImpact": {
                            "avatarUrl": "https://static.avito.ru/stub_avatars/%D0%97/13_256x256.png",
                            "data": {
                                "co2": 0,
                                "energy": 0,
                                "materials": 0,
                                "pineYears": 0,
                                "water": elem
                            }
                        }
                    },
                    "isAuthorized": True
                },
                "status": "ok"
            })
            route.fulfill(
                status=200,
                body=new_response,
                headers={"Content-Type": "application/json"}
            )

        page.route('https://www.avito.ru/web/1/charity/ecoImpact/init', intercept)

        page.locator(".desktop-impact-item-eeQO3:nth-child(4)").screenshot(path="output/W-{0}.png".format(i + 1))
        time.sleep(2)

def test_co2(page: Page):

    a = [1, 999, 1000, 1001, 9954, 9955, 10000, 10001, 10049, 10050, 99950, 100000, 100499, 100500, 999449, 999500,
          1000000, 1044000, 1045000, 999449000, 999500000, 1000000000]
    for i, elem in enumerate(a):
        page.goto("https://www.avito.ru/avito-care/eco-impact", wait_until="domcontentloaded")
        def intercept(route):
            new_response = json.dumps({
                "result": {
                    "blocks": {
                        "personalImpact": {
                            "avatarUrl": "https://static.avito.ru/stub_avatars/%D0%97/13_256x256.png",
                            "data": {
                                "co2": elem,
                                "energy": 0,
                                "materials": 0,
                                "pineYears": 0,
                                "water": 0
                            }
                        }
                    },
                    "isAuthorized": True
                },
                "status": "ok"
            })
            route.fulfill(
                status=200,
                body=new_response,
                headers={"Content-Type": "application/json"}
            )
        page.route('https://www.avito.ru/web/1/charity/ecoImpact/init', intercept)
        page.locator(".desktop-impact-item-eeQO3:nth-child(2)").screenshot(path="output/CO2-{0}.png".format(i + 1))
        time.sleep(2)


def test_energy(page: Page):

    a = [1, 999, 1000, 1001, 9954, 9955, 10000, 10001, 10049, 10050, 99950, 100000, 100499, 100500, 999449, 999500,
          1000000, 1044000, 1045000, 999449000, 999500000, 1000000000]
    for i, elem in enumerate(a):
        page.goto("https://www.avito.ru/avito-care/eco-impact", wait_until="domcontentloaded")

        def intercept(route):
            new_response = json.dumps({
                "result": {
                    "blocks": {
                        "personalImpact": {
                            "avatarUrl": "https://static.avito.ru/stub_avatars/%D0%97/13_256x256.png",
                            "data": {
                                "co2": 0,
                                "energy": elem,
                                "materials": 0,
                                "pineYears": 0,
                                "water": 0
                            }
                        }
                    },
                    "isAuthorized": True
                },
                "status": "ok"
            })
            route.fulfill(
                status=200,
                body=new_response,
                headers={"Content-Type": "application/json"}
            )
        page.route('https://www.avito.ru/web/1/charity/ecoImpact/init', intercept)
        page.locator(".desktop-impact-item-eeQO3:nth-child(6)").screenshot(path="output/E-{0}.png".format(i + 1))
        time.sleep(2)