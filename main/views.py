from django.shortcuts import render

def show_main(request):
    context = {
        'title': 'Welcome To Our Nakama Collective',
        'creator': 'Created by Serafina Nala Putri Setiawan - KKI ',
        'best_seller': "Luffy's Strawhat - 45k",
        'best_seller_image': "https://onepiece-universe.com/wp-content/uploads/2022/01/cosplay-luffy-hat-3-1000x1000.jpg",
        'nakama_collection': [
            "Nami's Temporary Tattoo - 20k",
            "Franky's Super Sunglasses - 55k",
            "Sanji's Cigarette Lighter - 75k",
            "Chopper's Mega Plushy - 120k",
            "Brook's Magnificent Music Box - 210k",
            "Robin's Brilliant Boots - 350k",
            "Jinbe's Classic Coat - 410k",
        ],
        'limited_offer': "Zoro's Special Edition Enma - 750k",
        'limited_offer_image': "https://media.karousell.com/media/photos/products/2020/9/19/one_piece_roronoa_zoro_enma_sw_1600483488_bd4edec4_progressive.jpg",
        'main_image': "https://www.crunchyroll.com/imgsrv/display/thumbnail/1200x675/catalog/crunchyroll/1ecde018e863e2aaee31f00a23378c35.jpe",
    }
    return render(request, "main.html", context)
