URL_PRICES = 'https://kolgotki-opt.ru/blanki-zakaza/'
URL_BASE = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'

# FOLDER = 'z:/Work/Inet/RM/Help/Базовые прайсы/Колготки/НЬюлайн/Остатки/'
FOLDER = 'data/'
FILE_PRICES = (
    ('Леггинсы и джинсы', '19 leggins.xlsx'),
    ('Колготки КЛАССИКА', '1 kolgotki.xlsx'),
    ('Колготки ДЕТСКИЕ', '11 kolgotki det.xlsx'),
    ('Колготки ФАНТАЗИЯ', '1 kolgotki 2.xlsx'),
    ('Нижнее белье (ИТАЛИЯ)', '3 korsetnoe(italia,espania).xlsx'),
    ('Бесшовное бельё', '2 intimidea.xlsx'),
    ('Домашняя одежда', '10 angel stori.xlsx'),
    # ('Эльдар (трикотаж)', '9 eldar.xlsx'),
    ('Белье МУЖСКОЕ', '6 griff muzckoe.xlsx'),
    ('Белье корректирующее и классическое (MITEX)', '7 mitex.xlsx'),
    # ('Носки,тапки', '17 noskitap.xlsx'),
    ('Купальники', '8 kypalniki.xlsx'),
    # ('Наушники HOBBY LINE', '16 Nausniki.xlsx'),
    # ('Сувениры новогодние', '15 suvenir.xlsx'),
    ('OPIUM SPORT', '14 varezki.xlsx'),  # Подмена файла
    ('Носки мужские, женские, детские', '12 noski.xlsx'),
    ('Поясное белье женские (ПЛАВКИ)', '5 malemi.xlsx'),
    # ('Бельё DIVA SHARM прибалтика (большие размеры)', '18 DIVA.xlsx'),
    ('Термобельё', '4 termobelio.xlsx'),
    # ('ДЕТСКОЕ шапки, перчатки', '20 SHAPKI.xlsx'),
    ('Домашняя обувь', '21 dom.obuv.xlsx'),
)

PRODUCT_SIGN_COLUMN = 1
PRODUCT_IMAGE_COLUMN = 2
PRODUCT_NAME_COLUMN = 4
PRODUCT_SIZE_RANGE = range(15, 24)
PRODUCT_PRICE_COLUMN = 36
PRODUCT_COLOR_COLUMN = 4
PRODUCT_START_REMAINS_COLUMN = 15
PRODUCT_SKIP_HEAD_ROWS = range(7)
