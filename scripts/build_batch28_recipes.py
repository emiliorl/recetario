import json
from pathlib import Path

RECIPES_DIR = Path("cache/recipes")
RECIPES_DIR.mkdir(parents=True, exist_ok=True)

# 1. Update source_refs for existing merged recipes
merged_updates = {
    "70_1.json": ["70#1", "226#1", "230#1"],
    "71_1.json": ["71#1", "226#2", "230#2"],
    "73_1.json": ["73#1", "224#1"],
    "90_1.json": ["90#1", "228#1"],
    "91_1.json": ["91#1", "233#1"],
    "92_1.json": ["92#1", "226-1#1"],
    "93_1.json": ["93#1", "223#1"],
    "95_1.json": ["95#1", "227#1"],
    "103_1.json": ["103#1", "231#1"]
}

for fname, refs in merged_updates.items():
    fpath = RECIPES_DIR / fname
    if fpath.exists():
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)
        data["source_refs"] = refs
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(f"Updated source_refs for {fname}: {refs}")

# 2. Define new batch 28 recipes and tips
new_items = {
    "216_1.json": {
        "cluster": "216#1",
        "kind": "recipe",
        "source_refs": ["216#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Ambrosia sauce",
            "category": "Salsas y aderezos",
            "tags": ["salsa dulce", "frutas", "postres"],
            "servings": "6 porciones",
            "prep_time": "10 min",
            "cook_time": "10 min",
            "temperature": "",
            "ingredient_groups": [
                {
                    "name": "",
                    "items": [
                        "1 Taza de piña triturada en su jugo",
                        "1 Taza de gajos de mandarinas escurridas",
                        "1/2 Taza de coco rallado",
                        "2 Cucharadas de azúcar",
                        "1 Cucharada de maicena",
                        "2 Cucharadas de jugo de naranja o agua",
                        "1 Cucharadita de jugo de limón"
                    ]
                }
            ],
            "steps": [
                "Disolver la maicena en 2 cucharadas de jugo de naranja o agua.",
                "En una olla pequeña a fuego medio, combinar la piña con su jugo, las mandarinas escurridas, el coco rallado y el azúcar.",
                "Añadir la maicena disuelta y el jugo de limón.",
                "Cocinar revolviendo constantemente hasta que la salsa espese y tome un hervor suave y brillante.",
                "Retirar del fuego y servir tibia o fría sobre pasteles, bizcochos o helado."
            ],
            "teacher_notes": [],
            "notes": [
                "Salsa frutal aromática para bañar queques, bizcochos o helados."
            ]
        }
    },
    "216_2.json": {
        "cluster": "216#2",
        "kind": "recipe",
        "source_refs": ["216#2"],
        "source_hash": "manual",
        "recipe": {
            "title": "Salsa de naranja para postres",
            "category": "Salsas y aderezos",
            "tags": ["salsa dulce", "cítricos", "postres"],
            "servings": "6 porciones",
            "prep_time": "5 min",
            "cook_time": "8 min",
            "temperature": "",
            "ingredient_groups": [
                {
                    "name": "",
                    "items": [
                        "1/2 Taza de azúcar",
                        "1 Cucharada de maicena",
                        "1 Taza de jugo de naranja natural",
                        "1 Cucharadita de jugo de limón",
                        "Ralladura de 1 naranja",
                        "1 Cucharada de mantequilla"
                    ]
                }
            ],
            "steps": [
                "Mezclar el azúcar con la maicena en una cacerola pequeña.",
                "Incorporar gradualmente el jugo de naranja natural, el jugo de limón y la ralladura fina de naranja.",
                "Llevar a fuego medio sin dejar de mover hasta que hierva y tome consistencia espesa y translúcida.",
                "Retirar del fuego y agregar la cucharada de mantequilla, batiendo hasta derretir por completo.",
                "Servir tibia sobre crepes, panqueques o queques."
            ],
            "teacher_notes": [],
            "notes": []
        }
    },
    "217_1.json": {
        "cluster": "217#1",
        "kind": "recipe",
        "source_refs": ["217#1", "218#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Pasta básica para crepes dulces",
            "category": "Panes y masas",
            "tags": ["crepes", "masa básica", "postres"],
            "servings": "18-20 crepes",
            "prep_time": "15 min",
            "cook_time": "15 min",
            "temperature": "",
            "ingredient_groups": [
                {
                    "name": "",
                    "items": [
                        "1 Taza de harina cernida",
                        "1/4 Cucharadita de sal",
                        "1 Cucharada de azúcar",
                        "3 Huevos ligeramente batidos",
                        "1 1/2 Taza de leche",
                        "2 Cucharadas de mantequilla derretida"
                    ]
                }
            ],
            "steps": [
                "Cernir juntos la harina, la sal y el azúcar en un tazón.",
                "Aparte, batir ligeramente los huevos y mezclar con la leche y la mantequilla derretida.",
                "Incorporar los líquidos poco a poco a los ingredientes secos, batiendo vigorosamente para evitar grumos, hasta tener una masa lisa y suave.",
                "Dejar reposar la masa en refrigeración durante al menos 30 minutos.",
                "Calentar una crepera o sartén antiadherente ligeramente enmantequillada a fuego medio.",
                "Verter una porción delgada de masa girando la sartén para cubrir todo el fondo.",
                "Cocinar unos segundos hasta que los bordes se despeguen ligeramente, voltear con cuidado para cocinar el otro lado y retirar."
            ],
            "teacher_notes": [],
            "notes": [
                "Rendimiento indicado en anotación manuscrita: 18 a 20 crepes finas."
            ]
        }
    },
    "217_2.json": {
        "cluster": "217#2",
        "kind": "recipe",
        "source_refs": ["217#2", "218#2"],
        "source_hash": "manual",
        "recipe": {
            "title": "Crepes flambeadas (Crepes flambée)",
            "category": "Postres y pasteles",
            "tags": ["crepes", "flambeado", "cítricos", "elegante"],
            "servings": "4-6 porciones",
            "prep_time": "15 min",
            "cook_time": "10 min",
            "temperature": "",
            "ingredient_groups": [
                {
                    "name": "",
                    "items": [
                        "18-20 Crepes preparadas",
                        "4 Cucharadas de mantequilla",
                        "1/2 Taza de azúcar",
                        "1 Taza de jugo de naranja natural",
                        "2 Cucharadas de jugo de limón",
                        "1/4 Taza de licor de naranja (Grand Marnier o Cointreau)",
                        "1/4 Taza de ron dorado para flambear"
                    ]
                }
            ],
            "steps": [
                "En una sartén amplia a fuego bajo, derretir la mantequilla y disolver el azúcar junto con el jugo de naranja y el jugo de limón hasta formar un almíbar suave.",
                "Doblar cada crepe en cuatro (forma de pañuelo o abanico triangular) e ir acomodándolas en la sartén para que se impregnen y calienten en el almíbar.",
                "Rociar por encima el licor de naranja y el ron ligeramente tibio.",
                "Con mucho cuidado y manteniendo distancia segura, encender para flambear, permitiendo que las llamas doren el azúcar y consuman el alcohol.",
                "Servir de inmediato bien calientes con la salsa de la sartén."
            ],
            "teacher_notes": [],
            "notes": [
                "Receta de inspiración polinesia/francesa para ocasiones especiales."
            ]
        }
    },
    "217_3.json": {
        "cluster": "217#3",
        "kind": "recipe",
        "source_refs": ["217#3", "218#3"],
        "source_hash": "manual",
        "recipe": {
            "title": "Crepes ensueño de limón",
            "category": "Postres y pasteles",
            "tags": ["crepes", "limón", "cítricos", "postres"],
            "servings": "4-6 porciones",
            "prep_time": "10 min",
            "cook_time": "10 min",
            "temperature": "",
            "ingredient_groups": [
                {
                    "name": "",
                    "items": [
                        "12-16 Crepes preparadas",
                        "1 1/2 Taza de azúcar",
                        "1/2 Taza de jugo de limón natural",
                        "1 Cucharada de ralladura fina de limón",
                        "3 Cucharadas de mantequilla"
                    ]
                }
            ],
            "steps": [
                "En una sartén grande a fuego medio-bajo, fundir la mantequilla y añadir la 1 1/2 taza de azúcar, el jugo de limón y la ralladura de limón.",
                "Cocinar revolviendo suavemente hasta que el azúcar se disuelva por completo y comience a formar un jarabe aromático y translúcido.",
                "Doblar las crepes en cuatro y colocarlas en la sartén sumergiéndolas en el jarabe caliente de limón para que absorban todo su sabor.",
                "Dejar calentar 2 minutos y servir calientes bañadas con el almíbar cítrico."
            ],
            "teacher_notes": [],
            "notes": [
                "Anotación manuscrita al pie: 1 1/2 taza de azúcar, al fuego el limón."
            ]
        }
    },
    "219_1.json": {
        "cluster": "219#1",
        "kind": "recipe",
        "source_refs": ["219#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Galletas suizas de mantequilla",
            "category": "Postres y pasteles",
            "tags": ["galletas", "mantequilla", "nueces", "navidad"],
            "servings": "25-30 galletas",
            "prep_time": "20 min",
            "cook_time": "15 min",
            "temperature": "350°F (175°C)",
            "ingredient_groups": [
                {
                    "name": "",
                    "items": [
                        "1 Taza de mantequilla sin sal (a temperatura ambiente)",
                        "1/2 Taza de azúcar glass cernida",
                        "1 Huevo",
                        "2 Tazas de harina de trigo cernida",
                        "1/2 Taza de nueces o almendras finamente picadas",
                        "Coco rallado fino o extracto de vainilla al gusto"
                    ]
                }
            ],
            "steps": [
                "Precalentar el horno a 350°F (175°C).",
                "Batir la mantequilla hasta que esté muy cremosa y pálida; agregar el azúcar glass cernida poco a poco hasta integrar.",
                "Añadir el huevo y batir hasta lograr una textura homogénea.",
                "Incorporar la harina cernida con movimientos suaves hasta formar una masa suave y manejable.",
                "Agregar las nueces o almendras picadas (o coco rallado y esencia).",
                "Formar rollitos o pequeñas bolitas con las manos y rodarlas por más nueces picadas o coco rallado.",
                "Disponer en latas para hornear y hornear de 12 a 15 minutos, hasta que las bases estén ligeramente doradas pero la superficie clara.",
                "Dejar enfriar completamente sobre una rejilla."
            ],
            "teacher_notes": [],
            "notes": []
        }
    },
    "219_2.json": {
        "cluster": "219#2",
        "kind": "recipe",
        "source_refs": ["219#2"],
        "source_hash": "manual",
        "recipe": {
            "title": "Galletas básicas para cortar (y variaciones festivas)",
            "category": "Postres y pasteles",
            "tags": ["galletas", "masa para cortar", "navidad", "decoración"],
            "servings": "35-40 galletas",
            "prep_time": "30 min",
            "cook_time": "10 min",
            "temperature": "375°F (190°C)",
            "ingredient_groups": [
                {
                    "name": "",
                    "items": [
                        "1 Taza de margarina o mantequilla",
                        "1 Taza de azúcar",
                        "2 Huevos",
                        "1 Cucharadita de extracto de vainilla",
                        "3 Tazas de harina de trigo",
                        "2 Cucharaditas de polvo de hornear",
                        "1/2 Cucharadita de sal"
                    ]
                }
            ],
            "steps": [
                "Cremar la margarina con el azúcar con batidora hasta que esponje. Agregar los huevos uno a uno y la vainilla.",
                "Cernir juntos la harina, el polvo de hornear y la sal.",
                "Incorporar los ingredientes secos a la mezcla cremosa hasta obtener una masa uniforme que no se pegue a las manos.",
                "Envolver en plástico y refrigerar al menos 1 hora para que tome consistencia.",
                "Precalentar el horno a 375°F (190°C).",
                "Extender la masa con rodillo sobre superficie limpia y enharinada hasta 5 mm de grosor. Cortar con cortadores con formas de árboles navideños o figuras festivas.",
                "Colocar en bandejas para hornear y hornear de 8 a 10 minutos.",
                "Dejar enfriar antes de decorar con glasé real."
            ],
            "teacher_notes": [],
            "notes": [
                "Variaciones: Galletas morenas (sustituyendo parte del azúcar por morena y agregando canela), y galletas festivas decoradas con glasé de colores."
            ]
        }
    },
    "220_1.json": {
        "cluster": "220#1",
        "kind": "recipe",
        "source_refs": ["220#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Pastel navideño de ciruela y manzana",
            "category": "Postres y pasteles",
            "tags": ["pastel navideño", "especias", "manzana", "ciruelas", "fiestas"],
            "servings": "12-14 porciones",
            "prep_time": "25 min",
            "cook_time": "75 min",
            "temperature": "350°F (175°C)",
            "ingredient_groups": [
                {
                    "name": "",
                    "items": [
                        "2 Tazas de harina de trigo",
                        "1 1/2 Taza de azúcar",
                        "1 Cucharadita de bicarbonato de sodio",
                        "1 Cucharadita de canela en polvo",
                        "1/2 Cucharadita de pimienta gorda molida (allspice)",
                        "1/2 Cucharadita de sal",
                        "3 Huevos",
                        "1 Taza de aceite vegetal",
                        "1 Taza de puré de manzana",
                        "1 Taza de ciruelas pasas sin semilla, picadas",
                        "1 Taza de nueces picadas"
                    ]
                }
            ],
            "steps": [
                "Precalentar el horno a 350°F (175°C). Engrasar y enharinar generosamente un molde de chimenea o corona.",
                "Cernir juntos en un tazón grande la harina, el azúcar, bicarbonato de sodio, canela, pimienta gorda molida y sal.",
                "En otro recipiente, batir ligeramente los huevos, agregar el aceite y el puré de manzana, mezclando hasta integrar bien.",
                "Verter los líquidos sobre los ingredientes secos y mezclar con cuchara o espátula solo hasta humedecer la harina.",
                "Enharinar ligeramente las ciruelas pasas picadas y las nueces para distribuirlas uniformemente en la masa de manera envolvente.",
                "Verter la mezcla en el molde preparado y hornear a 350°F por 1 hora a 1 hora y 15 minutos, hasta que al insertar un palillo salga limpio.",
                "Dejar enfriar en el molde 15 minutos, luego desmoldar con cuidado sobre una rejilla."
            ],
            "teacher_notes": [],
            "notes": [
                "Receta de Beatrice's Kitchen para celebraciones navideñas."
            ]
        }
    },
    "221_1.json": {
        "cluster": "221#1",
        "kind": "recipe",
        "source_refs": ["221#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Pan de limón navideño con jarabe",
            "category": "Postres y pasteles",
            "tags": ["pan de molde", "cítricos", "limón", "navidad", "jarabe"],
            "servings": "2 panes medianos",
            "prep_time": "20 min",
            "cook_time": "45 min",
            "temperature": "350°F (175°C)",
            "ingredient_groups": [
                {
                    "name": "Masa del pan",
                    "items": [
                        "2 Tazas de harina de trigo",
                        "1 1/2 Cucharaditas de polvo de hornear",
                        "1/4 Cucharadita de sal",
                        "1/2 Taza de mantequilla o margarina (4 oz / 1 barra)",
                        "1 Taza de azúcar",
                        "2 Huevos",
                        "1/3 Taza de leche",
                        "2 Cucharaditas de ralladura fina de limón",
                        "1/2 Taza de nueces picadas"
                    ]
                },
                {
                    "name": "Jarabe de limón",
                    "items": [
                        "1/2 Taza de jugo de limón natural",
                        "1/3 Taza de azúcar"
                    ]
                }
            ],
            "steps": [
                "Precalentar el horno a 350°F (175°C). Engrasar y enharinar dos moldes rectangulares de pan de 7 x 3 1/2 x 2 pulgadas.",
                "Batir la mantequilla con la taza de azúcar hasta lograr una textura cremosa y esponjosa.",
                "Añadir los huevos uno a uno, batiendo bien tras cada adición.",
                "Cernir juntos la harina con el polvo de hornear y la sal; agregarlos a la mantequilla alternando poco a poco con la leche.",
                "Incorporar de forma envolvente las nueces picadas y la ralladura de limón.",
                "Distribuir la masa equitativamente en los dos moldes de pan y colocarlos sobre una bandeja para galletas.",
                "Hornear a 350°F durante 45 minutos.",
                "Para el jarabe: en una ollita pequeña combinar la 1/2 taza de jugo de limón y el 1/3 taza de azúcar; llevar al fuego revolviendo constantemente por un minuto hasta disolver el azúcar por completo.",
                "Inmediatamente al sacar los panes calientes del horno, verter el jarabe sobre ellos permitiendo que penetre en la miga.",
                "Dejar reposar 10 minutos dentro de los moldes y luego desmoldar para enfriar por completo sobre una parrilla."
            ],
            "teacher_notes": [
                "Cátedra de Beatriz de Arzú en el Instituto Femenino de Estudios Superiores (Arte Culinario - Técnicas Dulces). Hornear los moldes sobre una lata de galletas asegura un calor uniforme sin quemar la base."
            ],
            "notes": []
        }
    },
    "222_1.json": {
        "cluster": "222#1",
        "kind": "recipe",
        "source_refs": ["222#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Carne con vino tinto y champiñones",
            "category": "Platos principales",
            "tags": ["carne de res", "lomito", "vino tinto", "champiñones", "estofado"],
            "servings": "6 porciones",
            "prep_time": "20 min",
            "cook_time": "45 min",
            "temperature": "",
            "ingredient_groups": [
                {
                    "name": "",
                    "items": [
                        "2 Libras de lomito o rochoy cortado en cubos",
                        "1/4 Taza de mantequilla",
                        "1/2 Libra de hongos (champiñones) en tajadas",
                        "6 Tiras de tocino cortadas en cuadritos",
                        "2 Cucharadas de harina",
                        "1 Cucharadita de azúcar",
                        "1 Hoja de laurel",
                        "Tomillo seco al gusto",
                        "Sal y pimienta al gusto",
                        "1 Taza de vino tinto seco",
                        "1 Taza de caldo de res (consomé)",
                        "Cebolla finamente picada al gusto"
                    ]
                }
            ],
            "steps": [
                "En una cacerola con la mantequilla sofría la cebolla picada y los hongos en tajadas por 4 minutos; apartar.",
                "En la misma cacerola, freír el tocino en cuadritos hasta que quede bien crujiente; apartar el tocino y reservar la grasa en la cacerola.",
                "Sazonar los cubos de carne con sal y dorarlos a fuego vivo en la grasa del tocino hasta sellar todos sus lados.",
                "Espolvorear la harina sobre la carne y agregar la cucharadita de azúcar, el tomillo, sal al gusto y la hoja de laurel, revolviendo bien para tostar la harina.",
                "Verter el vino tinto seco y el caldo de res caliente.",
                "Tapar y cocer a fuego lento revolviendo de vez en cuando hasta que la carne esté perfectamente tierna y suave.",
                "Incorporar los hongos y el tocino frito reservados. Si el líquido se redujera demasiado, agregar un poco más de caldo o vino.",
                "Rectificar la sazón y servir caliente sobre una cama de arroz blanco."
            ],
            "teacher_notes": [
                "Cátedra de AEH. Margarita de Sánchez en el IFES (Hogar Empresa II - Arte Culinario)."
            ],
            "notes": []
        }
    },
    "229_1.json": {
        "cluster": "229#1",
        "kind": "recipe",
        "source_refs": ["229#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Potpurri de vegetales con albahaca y pimiento",
            "category": "Entradas y bocadillos",
            "tags": ["vegetales", "guarnición", "saludable", "vapor"],
            "servings": "4-6 porciones",
            "prep_time": "15 min",
            "cook_time": "15 min",
            "temperature": "",
            "ingredient_groups": [
                {
                    "name": "",
                    "items": [
                        "1 Taza de arvejas tiernas peladas",
                        "1 Taza de ejotes cortados en trozos",
                        "1 Coliflor grande cortada en florecitas pequeñas",
                        "3/4 Taza de agua",
                        "1 Lata de chiles pimientos en tiras",
                        "2 Cucharadas de mantequilla o margarina",
                        "1/2 Cucharadita de albahaca seca",
                        "1/2 Cucharadita de sal",
                        "1/2 Cucharadita de pimienta negra"
                    ]
                }
            ],
            "steps": [
                "Colocar las arvejas, ejotes y florecitas de coliflor en una olla con los 3/4 taza de agua hirviendo o en vaporera, y cocinar hasta que estén tiernos pero crujientes (al dente).",
                "Escurrir completamente el agua de cocción.",
                "Añadir a las verduras calientes los chiles pimientos en tiras, la mantequilla o margarina, la albahaca seca, sal y pimienta.",
                "Saltear suavemente hasta que la mantequilla se funda y sazone todos los vegetales uniformemente. Servir caliente."
            ],
            "teacher_notes": [],
            "notes": [
                "Receta de Beatrice's Kitchen."
            ]
        }
    },
    "229_2.json": {
        "cluster": "229#2",
        "kind": "recipe",
        "source_refs": ["229#2"],
        "source_hash": "manual",
        "recipe": {
            "title": "Zanahorias baby glaseadas con naranja y azúcar morena",
            "category": "Entradas y bocadillos",
            "tags": ["zanahorias", "glaseado", "guarnición", "cítricos"],
            "servings": "4-6 porciones",
            "prep_time": "10 min",
            "cook_time": "15 min",
            "temperature": "",
            "ingredient_groups": [
                {
                    "name": "",
                    "items": [
                        "1 1/4 Libras de zanahorias baby",
                        "1/3 Taza de azúcar morena",
                        "2 Cucharadas de mantequilla o margarina",
                        "1/2 Cucharadita de sal",
                        "1/2 Cucharadita de ralladura fina de naranja"
                    ]
                }
            ],
            "steps": [
                "Cocinar las zanahorias baby en poca agua hirviendo sin sal o al vapor hasta que estén tiernas pero firmes; escurrir bien.",
                "En una sartén amplia u olla, colocar el azúcar morena, la mantequilla o margarina, la sal y la ralladura de naranja.",
                "Calentar a fuego medio hasta que la mantequilla y el azúcar se fundan formando burbujas parejas.",
                "Añadir las zanahorias baby cocidas y saltear a fuego suave durante unos 5 minutos, revolviendo ocasionalmente para que adquieran un glaseado brillante, almibarado y uniforme.",
                "Servir calientes como acompañamiento para carnes o aves."
            ],
            "teacher_notes": [],
            "notes": [
                "Receta de Beatrice's Kitchen."
            ]
        }
    },
    "232_1.json": {
        "cluster": "232#1",
        "kind": "recipe",
        "source_refs": ["232#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Tiramisú tradicional con queso mascarpone",
            "category": "Postres y pasteles",
            "tags": ["postre frío", "café", "mascarpone", "italiano"],
            "servings": "8-10 porciones",
            "prep_time": "30 min",
            "cook_time": "0 min",
            "temperature": "",
            "ingredient_groups": [
                {
                    "name": "",
                    "items": [
                        "2 Paquetes de queso mascarpone (aprox. 1 lb total)",
                        "3/4 Taza de crema para batir bien fría",
                        "3/4 Taza de azúcar",
                        "5 Cucharadas de café instantáneo disuelto espeso en poca agua caliente",
                        "1/2 a 3/4 Taza de licor de café (Kahlúa o licor similar)",
                        "1 Paquete grande de galletas chiquiadores (soletillas / vainillas)",
                        "Cocoa amarga pura en polvo para espolvorear"
                    ]
                }
            ],
            "steps": [
                "En un tazón hondo o plato extendido, mezclar el café concentrado espeso con el licor de café (de 1/2 a 3/4 taza).",
                "En otro tazón batir enérgicamente el queso mascarpone junto con la crema y el azúcar hasta lograr una textura suave, sedosa y consistente.",
                "Sumergir rápidamente los chiquiadores por ambos lados en la mezcla de café con licor (evitando que se desarmen por exceso de líquido) y acomodar una primera capa uniforme en el fondo de un molde pyrex rectangular.",
                "Extender una capa generosa de la mezcla cremosa de mascarpone sobre los chiquiadores.",
                "Espolvorear con ayuda de un colador fino una capa abundante de cocoa amarga.",
                "Repetir el procedimiento alternando capas de chiquiadores remojados, crema de queso y cocoa, hasta completar 3 capas de galletas y terminar con crema espolvoreada con cocoa.",
                "Llevar a refrigeración durante al menos 3 a 4 horas (o de un día para otro) para que tome consistencia firme."
            ],
            "teacher_notes": [
                "Cátedra de AEH. Margarita de Sánchez (IFES). En las notas de clase se ajusta la cantidad de crema a 3/4 taza y el café a 5 cucharadas espesas para balancear la firmeza del postre."
            ],
            "notes": []
        }
    },
    "234_1.json": {
        "cluster": "234#1",
        "kind": "recipe",
        "source_refs": ["234#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Pastel de especias y jengibre con mieles",
            "category": "Postres y pasteles",
            "tags": ["pastel", "jengibre", "canela", "especias", "miel"],
            "servings": "10-12 porciones",
            "prep_time": "20 min",
            "cook_time": "30 min",
            "temperature": "350°F (175°C)",
            "ingredient_groups": [
                {
                    "name": "",
                    "items": [
                        "1/2 Taza de mantequilla",
                        "1/2 Taza de azúcar",
                        "1 Huevo grande",
                        "2 1/2 Tazas de harina de trigo",
                        "1 1/2 Cucharaditas de bicarbonato de sodio",
                        "1 Cucharadita de polvo de hornear (Royal)",
                        "1 Cucharadita de canela en polvo",
                        "1 1/2 Cucharaditas de jengibre molido",
                        "1/2 Cucharadita de sal",
                        "1/2 Taza de miel Karo (jarabe de maíz)",
                        "1/2 Taza de miel de abeja pura",
                        "1 Taza de agua caliente"
                    ]
                }
            ],
            "steps": [
                "Precalentar el horno a 350°F (175°C). Engrasar y enharinar un molde para hornear.",
                "Derretir la mantequilla; añadir el azúcar y el huevo batiendo muy bien hasta incorporar.",
                "Cernir juntos los ingredientes secos: harina, bicarbonato de sodio, polvo de hornear, canela, jengibre y sal.",
                "En una taza medidora para líquidos, mezclar la miel Karo, la miel de abeja y la taza de agua caliente hasta disolver.",
                "Incorporar a la mezcla de mantequilla y huevo los ingredientes secos y la mezcla tibia de mieles de forma alternada, comenzando y terminando con los secos.",
                "Verter la masa en el molde preparado y hornear a 350°F durante aproximadamente 30 minutos, hasta que al introducir un palillo salga limpio.",
                "Dejar enfriar antes de desmoldar."
            ],
            "teacher_notes": [],
            "notes": [
                "Recetas extra del recetario familiar."
            ]
        }
    },
    "234_2.json": {
        "cluster": "234#2",
        "kind": "recipe",
        "source_refs": ["234#2"],
        "source_hash": "manual",
        "recipe": {
            "title": "Bolas de camote con malvaviscos y nuez",
            "category": "Postres y pasteles",
            "tags": ["camote", "dulce tradicional", "malvaviscos", "nueces", "miel"],
            "servings": "10 unidades",
            "prep_time": "20 min",
            "cook_time": "25 min",
            "temperature": "300°F (150°C)",
            "ingredient_groups": [
                {
                    "name": "",
                    "items": [
                        "2 1/2 Tazas de puré de camote caliente",
                        "3 Onzas de mantequilla",
                        "1/2 Taza de azúcar",
                        "1/2 Cucharadita de sal",
                        "1 Cucharadita de extracto de vainilla",
                        "10 Angelitos blancos grandes (malvaviscos)",
                        "1/3 Taza de miel de abejas",
                        "2 Onzas de mantequilla derretida (para bañar)",
                        "1 Taza de nueces picadas"
                    ]
                }
            ],
            "steps": [
                "En un tazón hondo mezclar el puré de camote caliente con las 3 onzas de mantequilla, el azúcar, la sal y la vainilla hasta obtener una masa uniforme y manejable.",
                "Dividir la masa en 10 porciones; formar una bola con cada porción y colocar en su centro un malvavisco grande (angelito), cerrando bien la masa de camote alrededor para que quede completamente cubierto.",
                "Aparte, mezclar en un tazón pequeño las 2 onzas de mantequilla derretida con el 1/3 taza de miel de abeja.",
                "Pasar cada bola rellena por la mezcla de miel y mantequilla derretida, y rodarla inmediatamente en las nueces picadas presionando ligeramente para que queden bien empanizadas.",
                "Acomodar las bolas en una bandeja para hornear y hornear a 300°F durante 20 a 25 minutos.",
                "Servir tibias o a temperatura ambiente."
            ],
            "teacher_notes": [],
            "notes": [
                "Recetas extra del recetario familiar. Los 'angelitos' son malvaviscos."
            ]
        }
    },
    "235_1.json": {
        "cluster": "235#1",
        "kind": "tip",
        "source_refs": ["235#1"],
        "source_hash": "manual",
        "tip": {
            "title": "Programa de curso: Arte Culinario I - Técnicas y menús",
            "body": [
                "Instituto Femenino de Estudios Superiores (IFES) - Departamento de Hogar Empresa.\nHogar Empresa II - Primer Trimestre - Arte Culinario I. Catedrática: AEH. Margarita de Sánchez.\n\n**Objetivo**: Complementar de una forma más variada y elaborada en las recetas, a las clases de Técnicas Culinarias Saladas y Dulces. Así como ir elaborando menús balanceados y coordinados.",
                "### Módulos de técnicas culinarias\n\n* **Técnica de Pastas:** Fussilli con salsa de chile pimiento, Lasagna de pollo especial.\n* **Técnica de Crepas:** Crepas de pollo en salsa de hongos, Crepas dulces de fresa.\n* **Técnica de Pasteles Esponjosos:** Brazo Gitano, Pastel Esponjoso de Frutas.\n* **Técnica de Pies:** Pie de Puerro, Quiche Lorraine, Pie de Higo Especial.",
                "### Menús programados por temática\n\n* **Menú 1 Cuaresma:** Camarones Florentinos, Pastel de Banano.\n* **Menú 2 Cuaresma:** Pescado con chile pimiento, Atún en Cacerola, Pastel de Zanahoria.\n* **Menú 3 Cuaresma:** Pescado empanizado con salsa Tártara, Pastel de helado de café.\n* **Bar de Ensaladas.**\n* **Menú Especial:** Pollo en salsa de Albaricoques, Ensalada de espinaca y mandarinas, Brownies decorados con chocolate y helado."
            ]
        }
    }
}

for fname, data in new_items.items():
    fpath = RECIPES_DIR / fname
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {fpath}")

print("All batch 28 recipes and tips generated successfully.")
