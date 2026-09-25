import json
from pathlib import Path

RECIPES_DIR = Path("cache/recipes")
RECIPES_DIR.mkdir(parents=True, exist_ok=True)

# 1. Update 61_1.json (clusters 61#1 and 236#1)
recipe_61_path = RECIPES_DIR / "61_1.json"
if recipe_61_path.exists():
    with open(recipe_61_path, "r", encoding="utf-8") as f:
        data_61 = json.load(f)
else:
    data_61 = {"cluster": "61#1", "kind": "recipe", "recipe": {}}

data_61["cluster"] = "61#1"
data_61["kind"] = "recipe"
data_61["source_refs"] = ["61#1", "236#1"]
data_61["source_hash"] = "manual"
data_61["recipe"] = {
    "title": "Pescado con chile pimiento",
    "category": "Platos principales",
    "tags": ["pescado y mariscos", "horneado", "curvina", "pimientos morrones", "IFES"],
    "servings": "8-10 porciones",
    "prep_time": "15 min",
    "cook_time": "25 min",
    "temperature": "350°F (175°C)",
    "ingredient_groups": [
        {
            "name": "Base de pescado y cebolla",
            "items": [
                "10 Filetes de pescado fresco (curvina u otro pescado blanco) salpimentados",
                "2 Cebollas grandes cortadas en gajos",
                "Mantequilla para sofreír cebollas",
                "Sal y pimienta blanca al gusto"
            ]
        },
        {
            "name": "Salsa de morrón y gratinado",
            "items": [
                "1 Taza de crema pura",
                "1 Lata grande de chile pimiento morrón picado",
                "Queso parmesano rallado abundante para gratinar"
            ]
        }
    ],
    "steps": [
        "Sazonar los filetes de curvina con sal y pimienta blanca al gusto.",
        "En una sartén, freír los gajos de cebolla en mantequilla hasta que queden tiernos y translúcidos.",
        "Acomodar los filetes sazonados en una fuente refractaria (pyrex) y distribuir las cebollas salteadas por encima.",
        "Prehornear a 350°F por 5 minutos.",
        "Licuar la taza de crema con los chiles morrones de lata y una pizca de sal hasta obtener una crema rosada homogénea.",
        "Bañar los filetes con la salsa licuada y hornear a 350°F entre 15 y 20 minutos más.",
        "Espolvorear con queso parmesano rallado al gusto y gratinar brevemente hasta que dore."
    ],
    "teacher_notes": [
        "La curvina es ideal por su carne tierna y delicada; la combinación con la salsa cremosa de morrón le aporta un dulzor equilibrado y suave."
    ],
    "notes": [
        "Instituto Femenino de Estudios Superiores (IFES) - Catedrática AEH Margarita de Sánchez. Receta repetida en apuntes de clases en páginas 61 y 236."
    ]
}

with open(recipe_61_path, "w", encoding="utf-8") as f:
    json.dump(data_61, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(f"Updated {recipe_61_path}")


# 2. Update 105_2.json (clusters 105#2 and 252#1)
recipe_105_2_path = RECIPES_DIR / "105_2.json"
if recipe_105_2_path.exists():
    with open(recipe_105_2_path, "r", encoding="utf-8") as f:
        data_105_2 = json.load(f)
else:
    data_105_2 = {"cluster": "105#2", "kind": "recipe", "recipe": {}}

data_105_2["cluster"] = "105#2"
data_105_2["kind"] = "recipe"
data_105_2["source_refs"] = ["105#2", "252#1"]
data_105_2["source_hash"] = "manual"
data_105_2["recipe"] = {
    "title": "Pastel de chocolate especial",
    "category": "Postres y pasteles",
    "tags": ["al horno", "chocolate", "pastel", "fiestas", "repostería", "Edith's Kitchen"],
    "servings": "10-12 porciones",
    "prep_time": "25 min",
    "cook_time": "35 min",
    "temperature": "350°F (175°C)",
    "ingredient_groups": [
        {
            "name": "Masa de pastel de chocolate",
            "items": [
                "2 Tazas más 4 cucharadas de harina de trigo",
                "1 3/4 Tazas de azúcar",
                "1/4 Taza de cocoa amarga en polvo",
                "3/4 Cucharadita de sal",
                "1 1/2 Cucharadita de polvo de hornear (Royal)",
                "1 Cucharadita de bicarbonato de sodio",
                "3 Huevos enteros",
                "1 Cucharadita de extracto de vainilla",
                "3/4 Taza de leche líquida",
                "1/2 Taza de aceite vegetal"
            ]
        },
        {
            "name": "Armado y decoración",
            "items": [
                "Guindas (cerezas confitadas o al marrasquino)",
                "Almíbar de guindas espesado con un toque de fécula de maíz (maicena)",
                "Crema chantilly montada con azúcar glass y vainilla",
                "Galletas de chocolate trituradas (quebradas)"
            ]
        }
    ],
    "steps": [
        "Precalentar el horno a 350°F (175°C). Engrasar y enharinar un molde para pastel, colocando un círculo de papel encerado o parafinado en el fondo para garantizar un desmoldado perfecto.",
        "En un tazón grande, cernir y combinar todos los ingredientes secos: harina, azúcar, cocoa en polvo, sal, polvo para hornear y bicarbonato.",
        "Añadir los ingredientes líquidos: huevos, extracto de vainilla, leche y aceite vegetal.",
        "Batir con batidora eléctrica a velocidad media durante 2 a 3 minutos hasta obtener una mezcla lisa, sedosa y completamente homogénea.",
        "Verter la masa en el molde preparado.",
        "Hornear a 350°F durante aproximadamente 35 minutos, o hasta que al insertar un palillo en el centro salga limpio.",
        "Dejar enfriar 10 minutos en el molde, desmoldar sobre rejilla y dejar enfriar por completo.",
        "Para la decoración: batir crema dulce bien fría con azúcar glass y vainilla hasta lograr picos firmes de chantilly; en una ollita, calentar el almíbar de las guindas disuelto con un poco de maicena hasta espesar y dejar enfriar.",
        "Cubrir el pastel con la crema chantilly, espolvorear los laterales o cubierta con galleta de chocolate quebrada y decorar con las guindas abrillantadas.",
        "Decorar con rosetones de chantilly y guindas en la parte superior."
    ],
    "teacher_notes": [
        "Colocar un redondel de papel encerado en el fondo del molde engrasado y enharinado es fundamental en los pasteles de chocolate para evitar que la base se pegue o se reseque."
    ],
    "notes": [
        "Receta de Edith's Kitchen presente en páginas 105 y 252 del recetario."
    ]
}

with open(recipe_105_2_path, "w", encoding="utf-8") as f:
    json.dump(data_105_2, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(f"Updated {recipe_105_2_path}")


# 3. New recipes for Batch 29
new_recipes = [
    {
        "file": "237_1.json",
        "cluster": "237#1",
        "kind": "recipe",
        "source_refs": ["237#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Crepas dulces de fresa",
            "category": "Postres y pasteles",
            "tags": ["crepas", "fresas", "queso crema", "leche condensada", "postre", "Edith's Kitchen"],
            "servings": "8-10 porciones",
            "prep_time": "30 min",
            "cook_time": "15 min",
            "temperature": "Temperatura ambiente / baño María",
            "ingredient_groups": [
                {
                    "name": "Relleno y crepas",
                    "items": [
                        "1 Receta de crepas dulces preparadas",
                        "1 Barra (8 onzas) de queso crema suavizado (Pharma o Philadelphia)",
                        "1 Lata de leche condensada",
                        "1 Caja de fresas frescas lavadas y cortadas en cuadritos",
                        "Jugo fresco de 1 limón",
                        "Ralladura fina de 1 limón"
                    ]
                },
                {
                    "name": "Salsa de fresas y terminado",
                    "items": [
                        "2 Tazas de fresas frescas licuadas",
                        "2 Tazas de azúcar",
                        "Unas gotas de colorante vegetal rojo (opcional)",
                        "Crema Chantilly montada para decorar"
                    ]
                }
            ],
            "steps": [
                "Preparar las crepas dulces con antelación (se pueden elaborar desde un día antes y refrigerar tapadas).",
                "Para el relleno: batir el queso crema suavizado junto con la leche condensada, la ralladura y el jugo de limón hasta obtener una mezcla suave y homogénea.",
                "Incorporar suavemente las fresas picadas en cuadritos a la mezcla de queso crema.",
                "Rellenar cada una de las crepas con la preparación y acomodarlas enrolladas en una fuente refractaria (pyrex).",
                "Para la salsa: colocar en una cacerola las 2 tazas de fresas licuadas con las 2 tazas de azúcar y el colorante vegetal opcional. Llevar a fuego medio hasta que rompa el hervor y espese ligeramente.",
                "Bañar las crepas calientes o tibias con la salsa de fresas y decorar con rosetones de crema Chantilly fresca."
            ],
            "teacher_notes": [],
            "notes": ["Receta de Edith's Kitchen."]
        }
    },
    {
        "file": "238_1.json",
        "cluster": "238#1",
        "kind": "recipe",
        "source_refs": ["238#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Salsa de limón",
            "category": "Salsas y aderezos",
            "tags": ["salsa dulce", "limón", "postres", "coberturas", "cítricos"],
            "servings": "2/3 de taza (15 a 18 porciones)",
            "prep_time": "5 min",
            "cook_time": "10 min",
            "temperature": "Fuego lento",
            "ingredient_groups": [
                {
                    "name": "Ingredientes de la salsa",
                    "items": [
                        "1 Taza de azúcar",
                        "2 Cucharadas de maicena (fécula de maíz)",
                        "1 Taza de agua",
                        "1/4 Taza de mantequilla o margarina",
                        "2 Cucharaditas de ralladura fina de limón",
                        "1 Pizca de sal",
                        "1/4 Taza de jugo fresco de limón"
                    ]
                }
            ],
            "steps": [
                "En una olla mediana o cacerola, mezclar en seco el azúcar y la maicena para evitar grumos.",
                "Añadir la taza de agua poco a poco batiendo con batidor de alambre hasta disolver completamente.",
                "Llevar a ebullición a fuego medio, revolviendo constantemente.",
                "Reducir el fuego al mínimo y cocinar a fuego lento durante aproximadamente 5 minutos, hasta que la salsa adquiera consistencia espesa y aspecto transparente.",
                "Retirar de inmediato del fuego e incorporar la mantequilla, la ralladura de limón, la pizca de sal y el jugo fresco de limón, batiendo hasta integrar.",
                "Servir tibia sobre budines, pasteles, helados o crepas."
            ],
            "teacher_notes": [],
            "notes": ["Rinde aproximadamente 2/3 de taza."]
        }
    },
    {
        "file": "239_1.json",
        "cluster": "239#1",
        "kind": "recipe",
        "source_refs": ["239#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Salsa de moras",
            "category": "Salsas y aderezos",
            "tags": ["salsa dulce", "moras", "frutos rojos", "canela", "postres"],
            "servings": "2 tazas",
            "prep_time": "5 min",
            "cook_time": "15 min",
            "temperature": "Fuego moderado",
            "ingredient_groups": [
                {
                    "name": "Ingredientes de la salsa",
                    "items": [
                        "1 Cucharadita de ralladura fina de limón",
                        "3 Tazas de moras frescas limpias",
                        "1 Cucharada de jugo de limón",
                        "3/4 Cucharadita de canela en polvo",
                        "1 1/2 Tazas de azúcar",
                        "1 Cucharadita de mantequilla o margarina"
                    ]
                }
            ],
            "steps": [
                "En una cacerola, colocar los ingredientes en el orden indicado: ralladura de limón, moras, jugo de limón, canela en polvo, azúcar y mantequilla.",
                "Llevar a la estufa a fuego moderado, mezclando suavemente para permitir que las moras liberen sus jugos naturales.",
                "Cocinar a fuego suave y constante hasta que el azúcar se disuelva y la preparación forme una salsa untuosa, suave y de hermoso brillo morado.",
                "Retirar del fuego y servir tibia o fría sobre cheesecakes, helados, panqueques o crepas."
            ],
            "teacher_notes": [],
            "notes": ["Rendimiento: 2 tazas de salsa."]
        }
    },
    {
        "file": "240_1.json",
        "cluster": "240#1",
        "kind": "recipe",
        "source_refs": ["240#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Salsa de caramelo",
            "category": "Salsas y aderezos",
            "tags": ["salsa dulce", "caramelo", "yemas", "canela", "tradicional"],
            "servings": "8-10 porciones",
            "prep_time": "10 min",
            "cook_time": "15 min",
            "temperature": "Fuego muy bajo",
            "ingredient_groups": [
                {
                    "name": "Ingredientes",
                    "items": [
                        "1 1/2 Tazas de azúcar",
                        "2 Tazas de leche líquida",
                        "12 Yemas de huevo bien batidas",
                        "1 Raja gruesa de canela"
                    ]
                }
            ],
            "steps": [
                "En una olla de fondo grueso, colocar el azúcar y calentar a fuego medio hasta fundirla y formar un caramelo claro y dorado.",
                "Retirar un momento de la llama y agregar con sumo cuidado la leche tibia, la raja de canela y las yemas batidas (incorporar batiendo continuamente para atemperar las yemas y evitar que coagulen por el choque de temperatura).",
                "Regresar a fuego muy bajo y continuar la cocción, revolviendo suavemente con cuchara de madera, hasta que el caramelo se disuelva por completo y la salsa tome cuerpo y sedosidad.",
                "Colar si fuera necesario para retirar cualquier grumo y la raja de canela.",
                "Dejar entibiar antes de servir como acompañamiento suntuoso para postres."
            ],
            "teacher_notes": [
                "Cuidado especial: la altísima temperatura del azúcar caramelizado puede cortar las yemas si no se vierten con rapidez y agitación constante."
            ],
            "notes": []
        }
    },
    {
        "file": "241_1.json",
        "cluster": "241#1",
        "kind": "recipe",
        "source_refs": ["241#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Salsa caliente de chocolate",
            "category": "Salsas y aderezos",
            "tags": ["salsa dulce", "chocolate", "helado", "postres", "microondas"],
            "servings": "6-8 porciones",
            "prep_time": "5 min",
            "cook_time": "5 min",
            "temperature": "Microondas Medium-Low o Baño María",
            "ingredient_groups": [
                {
                    "name": "Ingredientes",
                    "items": [
                        "1 Taza de chocolate semidulce (en trocitos, cobertura o chispas)",
                        "1/2 Taza de miel Karo blanca (jarabe de maíz)",
                        "1/4 Taza de crema pura de leche",
                        "1 Cucharada de mantequilla",
                        "1 Cucharadita de extracto de vainilla"
                    ]
                }
            ],
            "steps": [
                "En un tazón de vidrio apto para microondas (o a baño María), combinar el chocolate troceado y la miel Karo blanca.",
                "Calentar en el microondas a potencia Medium Low (potencia media baja) durante 4 a 4 1/2 minutos, vigilando que no se queme.",
                "Retirar y mezclar enérgicamente con batidor para fundir por completo el chocolate.",
                "Agregar poco a poco la crema pura sin dejar de revolver.",
                "Por último, incorporar la mantequilla y la vainilla hasta lograr una textura satinada, lisa y brillante.",
                "Servir caliente inmediatamente vertida sobre copas de helado de vainilla, brownies o crepas."
            ],
            "teacher_notes": [],
            "notes": [
                "En la hoja original aparece también una nota complementaria de galletas: colocar montoncitos de masa en lata forrada con papel parafinado, adornar con guindas y hornear a 325°F por 20 minutos (15 a 20 porciones)."
            ]
        }
    },
    {
        "file": "242_1.json",
        "cluster": "242#1",
        "kind": "recipe",
        "source_refs": ["242#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Tiramisú de fresa",
            "category": "Postres y pasteles",
            "tags": ["tiramisú", "fresas", "café expreso", "ron", "queso crema", "chocolate", "postre frío"],
            "servings": "4 dulceras individuales",
            "prep_time": "40 min",
            "cook_time": "0 min",
            "temperature": "Refrigeración",
            "ingredient_groups": [
                {
                    "name": "Fresas maceradas y base de café",
                    "items": [
                        "2 Vasos de fresas frescas machacadas",
                        "4 Cucharadas de ron oscuro (divididas: 1 cucharada para fresas, 3 para café)",
                        "16 Chiqueadores (soletillas o bizcochos de soletilla / ladyfingers)",
                        "3/4 Taza de café expreso preparado y frío"
                    ]
                },
                {
                    "name": "Crema y acabado",
                    "items": [
                        "1 Taza de queso crema suavizado",
                        "1 Taza de crema espesa para batir",
                        "1/3 Taza de azúcar",
                        "2 Onzas de chocolate semidulce rallado"
                    ]
                }
            ],
            "steps": [
                "En un tazón pequeño, combinar las fresas machacadas con 1 cucharada de ron oscuro; dejar marinar durante 30 minutos.",
                "Distribuir 4 chiqueadores en el fondo de cada una de las 4 dulceras o copas individuales de servir.",
                "En una taza o jarrita, mezclar el café expreso frío con las 3 cucharadas restantes de ron oscuro. Verter esta mezcla equitativamente sobre los chiqueadores para que se humedezcan.",
                "En un tazón mediano, combinar el queso crema suavizado, la crema espesa y el azúcar. Batir enérgicamente hasta obtener una crema aireada, firme y tersa.",
                "Repartir la crema sobre la capa de chiqueadores en cada copa.",
                "Colocar encima las fresas maceradas con sus jugos y coronar espolvoreando abundante chocolate semidulce rallado.",
                "Refrigerar antes de servir bien frío."
            ],
            "teacher_notes": [],
            "notes": []
        }
    },
    {
        "file": "243_1.json",
        "cluster": "243#1",
        "kind": "recipe",
        "source_refs": ["243#1", "244#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Crepas rellenas de manzana",
            "category": "Postres y pasteles",
            "tags": ["crepas", "manzana", "canela", "ron", "baño María", "postre", "Edith's Kitchen"],
            "servings": "15 porciones",
            "prep_time": "25 min",
            "cook_time": "25 min",
            "temperature": "Sartén y Baño María",
            "ingredient_groups": [
                {
                    "name": "Masa de crepas",
                    "items": [
                        "3 Huevos enteros",
                        "1 1/2 Tazas de leche líquida",
                        "1 1/4 Tazas de harina de trigo",
                        "1/2 Cucharadita de polvo de hornear (Royal)",
                        "2 Cucharadas de azúcar",
                        "1/8 Cucharadita de sal",
                        "2 Cucharadas de jugo fresco de limón",
                        "1 Cucharada de ron o cognac",
                        "Margarina derretida (para la masa y engrasar sartén)"
                    ]
                },
                {
                    "name": "Relleno de manzana especiada",
                    "items": [
                        "3 Libras de manzanas peladas y partidas en cuadritos",
                        "1/3 Taza de margarina",
                        "1/2 Taza de azúcar",
                        "1 Cucharadita de canela en polvo"
                    ]
                },
                {
                    "name": "Para servir",
                    "items": [
                        "1/4 Taza de azúcar",
                        "1 Cucharadita de canela en polvo"
                    ]
                }
            ],
            "steps": [
                "Para la masa de crepas: batir los huevos, añadir la leche y luego incorporar la harina cernida con el polvo para hornear, el azúcar y la sal, mezclando bien. Agregar un chorrito de margarina derretida, el jugo de limón y el ron o cognac hasta obtener un batido fino y fluido.",
                "Calentar una sartén mediana, untarla ligeramente con margarina y verter una porción de masa girando la sartén para cubrir solo el fondo con una capa delgada de orillas finas. Dorar ligeramente de un lado y dar vuelta para dorar el otro.",
                "Para el relleno: en una sartén grande o cacerola, derretir el tercio de taza de margarina; agregar los cuadritos de manzana, la media taza de azúcar y la cucharadita de canela. Cocinar a fuego mediano hasta que el jugo espese como almíbar y la manzana haya cambiado de color y esté suave.",
                "Rellenar cada crepa colocando una porción generosa del guisado de manzana en el centro, enrollar en forma cilíndrica y disponer en una bandeja a baño María para conservarlas bien calientes.",
                "Al momento de servir: acomodar las crepas calientes en un azafate y espolvorear generosamente con la mezcla de azúcar y canela molida."
            ],
            "teacher_notes": [],
            "notes": [
                "Receta de Edith's Kitchen dividida en las páginas 243 (masa y técnica) y 244 (relleno de manzana y presentación). Rinde 15 porciones."
            ]
        }
    },
    {
        "file": "245_1.json",
        "cluster": "245#1",
        "kind": "recipe",
        "source_refs": ["245#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Ensalada de pepino especial",
            "category": "Entradas y bocadillos",
            "tags": ["ensalada", "pepino", "pimientos", "crema", "mayonesa", "huevo duro", "fría", "Edith's Kitchen"],
            "servings": "6-8 porciones",
            "prep_time": "20 min (más 2 horas de reposo)",
            "cook_time": "5 min",
            "temperature": "Refrigerada / Fría",
            "ingredient_groups": [
                {
                    "name": "Vegetales y marinada",
                    "items": [
                        "4 Pepinos pelados y cortados en medias lunas (sin semillas)",
                        "3 Cebollas cortadas en gajos",
                        "2 Chiles pimientos cortados en tiritas pequeñas",
                        "1/2 Taza de vinagre",
                        "1/4 Taza de agua",
                        "Sal y pimienta al gusto"
                    ]
                },
                {
                    "name": "Aderezo cremoso",
                    "items": [
                        "1 Taza de crema fresca",
                        "1/2 Taza de mayonesa",
                        "2 Huevos duros finamente picaditos",
                        "Perejil fresco picado finamente",
                        "Sal y pimienta al gusto"
                    ]
                }
            ],
            "steps": [
                "Preparar una marinada mezclando en un tazón el vinagre, el agua, sal y pimienta al gusto.",
                "Colocar los pepinos cortados en medias lunas dentro de la marinada.",
                "Pasar las tiritas de chile pimiento rápidamente por agua hirviendo para blanquearlas; escurrir e incorporar a la marinada junto con los gajos de cebolla.",
                "Dejar reposar la mezcla en la vinagreta durante 2 horas en refrigeración para que los vegetales absorban todo el sabor y queden crujientes.",
                "Por aparte, en un tazón mezclar la mayonesa con la crema, los huevos duros picaditos, abundante perejil picado, sal y pimienta hasta lograr una salsa cremosa homogénea.",
                "Escurrir bien los pepinos, cebollas y pimientos de la vinagreta, y verterlos dentro de la mezcla cremosa.",
                "Integrar suavemente y servir bien fría."
            ],
            "teacher_notes": [],
            "notes": ["Receta de Edith's Kitchen."]
        }
    },
    {
        "file": "246_1.json",
        "cluster": "246#1",
        "kind": "recipe",
        "source_refs": ["246#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Pastel esponjoso de frutas",
            "category": "Postres y pasteles",
            "tags": ["pastel esponjoso", "bizcocho", "frutas", "crema pastelera", "almendras", "Edith's Kitchen"],
            "servings": "10-12 porciones",
            "prep_time": "35 min",
            "cook_time": "35 min",
            "temperature": "350°F (175°C)",
            "ingredient_groups": [
                {
                    "name": "Bizcochuelo esponjoso",
                    "items": [
                        "4 Huevos enteros",
                        "1/2 Taza más 1 cucharada de azúcar",
                        "1/2 Cucharadita de extracto de vainilla",
                        "1 Taza menos 2 cucharadas de harina de trigo cernida",
                        "7 Cucharadas de mantequilla derretida y refrescada"
                    ]
                },
                {
                    "name": "Almíbar y relleno",
                    "items": [
                        "Almíbar preparado con agua, azúcar, canela y cáscaras de limón o naranja",
                        "1 Receta de crema pastelera espesa (según receta página 248)"
                    ]
                },
                {
                    "name": "Decoración y brillo de frutas",
                    "items": [
                        "Frutas surtidas en almíbar bien escurridas (melocotones, guindas, higos, piña)",
                        "Almendras fileteadas tostadas",
                        "Jalea o mermelada de albaricoque",
                        "Un toque de gelatina sin sabor disuelta en agua (para el brillo)"
                    ]
                }
            ],
            "steps": [
                "En un tazón tibio (o puesto a baño María suave durante 5 minutos), batir los 4 huevos enteros junto con el azúcar y la vainilla hasta que espumen profusamente, tripliquen su volumen y alcancen punto de letra.",
                "Incorporar la harina cernida en forma suave y envolvente con espátula, cuidando no bajar el batido.",
                "Añadir por último las 7 cucharadas de mantequilla derretida a temperatura ambiente, incorporándola con sumo cuidado para evitar que se asiente en el fondo.",
                "Verter la masa en un molde redondo debidamente engrasado, enharinado y con un círculo de papel encerado en el fondo.",
                "Hornear a 350°F durante 30 a 35 minutos. Desmoldar de inmediato sobre una rejilla.",
                "Una vez frío el bizcocho, dividir horizontalmente, bañar con el almíbar cítrico y rellenar con la crema pastelera.",
                "Cubrir la superficie armoniosamente con las frutas escurridas y aplicarles el brillo elaborado disolviendo jalea de albaricoque tibia con gelatina sin sabor.",
                "Decorar los costados del pastel con las almendras fileteadas tostadas."
            ],
            "teacher_notes": [],
            "notes": ["Receta de Edith's Kitchen."]
        }
    },
    {
        "file": "247_1.json",
        "cluster": "247#1",
        "kind": "recipe",
        "source_refs": ["247#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Pie de puerro",
            "category": "Entradas y bocadillos",
            "tags": ["pie salado", "tarta", "puerro", "queso suizo", "al horno", "Edith's Kitchen"],
            "servings": "8 porciones",
            "prep_time": "25 min",
            "cook_time": "30 min",
            "temperature": "375°F (190°C)",
            "ingredient_groups": [
                {
                    "name": "Masa de pie salada",
                    "items": [
                        "2 Tazas de harina de trigo",
                        "2 Barras de margarina bien fría",
                        "1 Pizca de sal y 1 pizca de azúcar",
                        "Agua helada según sea necesario",
                        "Queso parmesano rallado para la masa"
                    ]
                },
                {
                    "name": "Relleno cremoso de puerros",
                    "items": [
                        "3 Tazas de puerros tiernos rebanados en rodajas finas",
                        "2 Cucharadas de mantequilla",
                        "1/2 Taza de crema pura",
                        "3 Huevos grandes bien batidos",
                        "1/2 a 1 Taza de queso suizo o queso pecorino rallado",
                        "Sal y pimienta molida al gusto"
                    ]
                }
            ],
            "steps": [
                "Preparar la masa de pie mezclando la harina con la sal, azúcar y queso parmesano; cortar la margarina fría hasta formar migas y unir con gotas de agua helada sin amasar en exceso. Forrar un molde para pie de 9 pulgadas.",
                "En una sartén, derretir las 2 cucharadas de mantequilla y saltear los puerros a fuego medio durante 3 a 4 minutos hasta que estén suaves y translúcidos. Añadir la media taza de crema y sazonar con sal y pimienta.",
                "En un tazón aparte, batir bien los huevos, incorporar el queso suizo o pecorino rallado y sazonar.",
                "Unir la mezcla de huevos y queso con los puerros tiernos en crema.",
                "Verter el relleno sobre la masa en el molde de pie.",
                "Hornear en horno precalentado a 375°F (190°C) durante 25 a 30 minutos, hasta que el relleno cuaje firmemente y la superficie esté ligeramente dorada."
            ],
            "teacher_notes": [],
            "notes": ["Receta de Edith's Kitchen."]
        }
    },
    {
        "file": "248_1.json",
        "cluster": "248#1",
        "kind": "recipe",
        "source_refs": ["248#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Crema pastelera rápida",
            "category": "Básicos y rellenos",
            "tags": ["crema pastelera", "relleno", "repostería", "amaretto", "kahlúa", "Edith's Kitchen"],
            "servings": "Aprox. 2 1/2 tazas",
            "prep_time": "10 min",
            "cook_time": "10 min",
            "temperature": "Fuego medio-bajo",
            "ingredient_groups": [
                {
                    "name": "Ingredientes",
                    "items": [
                        "1/2 Litro de leche entera",
                        "2 Yemas de huevo",
                        "4 Cucharadas colmadas de maicena (fécula de maíz)",
                        "1 Taza de azúcar cernida",
                        "1/2 Vaso de crema de leche",
                        "2 Onzas de mantequilla",
                        "1 Cucharadita de extracto de vainilla",
                        "1 Raja de canela",
                        "1 Pizca de sal",
                        "Licor de Amaretto o Kahlúa al gusto"
                    ]
                }
            ],
            "steps": [
                "Colocar en la licuadora la leche, las 2 yemas de huevo, la maicena, el azúcar cernida, la pizca de sal y el toque de licor (Amaretto o Kahlúa). Licuar brevemente hasta disolver por completo sin grumos.",
                "Verter el licuado en una cacerola, agregar la raja de canela entera y cocinar a fuego medio-bajo, revolviendo continuamente con cuchara de madera o batidor de alambre para que no se pegue en el fondo.",
                "Cocinar hasta que la crema rompa el hervor y espese con consistencia brillante.",
                "Retirar de inmediato del fuego, retirar y descartar la raja de canela.",
                "Añadir la vainilla, las 2 onzas de mantequilla y la crema de leche.",
                "Batir vigorosamente mientras se enfría para conferirle una textura aterciopelada y evitar que forme nata."
            ],
            "teacher_notes": [],
            "notes": [
                "Receta de Edith's Kitchen. Ideal para rellenar brazos gitanos, pasteles esponjosos, tartas y milhojas."
            ]
        }
    },
    {
        "file": "249_1.json",
        "cluster": "249#1",
        "kind": "recipe",
        "source_refs": ["249#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Brazo gitano",
            "category": "Postres y pasteles",
            "tags": ["brazo gitano", "arrollado", "cajeta de leche", "dulce de leche", "bizcocho", "Edith's Kitchen"],
            "servings": "10-12 porciones",
            "prep_time": "25 min",
            "cook_time": "15 min",
            "temperature": "350°F (175°C)",
            "ingredient_groups": [
                {
                    "name": "Masa de bizcochuelo",
                    "items": [
                        "7 Huevos grandes (separadas las claras de las yemas)",
                        "1 Taza de azúcar",
                        "1/2 Taza de harina de trigo cernida",
                        "1 Pizca de sal y unas gotas de agua (para ayudar a montar las claras)"
                    ]
                },
                {
                    "name": "Relleno y enrollado",
                    "items": [
                        "1 Lata de cajeta de leche (dulce de leche o manjar)",
                        "Azúcar glass abundante para espolvorear el paño",
                        "Papel parafinado para forrar el molde"
                    ]
                },
                {
                    "name": "Variación chocolate (opcional)",
                    "items": [
                        "1/4 Taza de cocoa amarga en polvo",
                        "2 Cucharaditas de ron oscuro"
                    ]
                }
            ],
            "steps": [
                "Separar cuidadosamente las claras de las yemas.",
                "Batir las claras con una pizca de sal y unas gotas de agua hasta alcanzar punto de nieve firme.",
                "Sin dejar de batir, añadir las yemas una a una, continuar batiendo, luego agregar gradualmente el azúcar.",
                "Por último, incorporar la harina cernida con movimientos envolventes muy suaves, o con la batidora en la velocidad mínima para no perder el aire.",
                "Engrasar y enharinar una lata grande para brazo gitano, forrada con papel parafinado.",
                "Extender la mezcla uniformemente y hornear a 350°F durante exactamente 15 minutos.",
                "Mientras tanto, extender sobre la mesa un limpiador o paño de cocina limpio y espolvorearlo generosamente con azúcar glass.",
                "Al sacar el bizcocho del horno, volcarlo inmediatamente sobre el paño espolvoreado y desprender con cuidado el papel parafinado.",
                "Untar de inmediato con la cajeta de leche y enrollar con ayuda del paño mientras aún esté caliente.",
                "Envolver bien y refrigerar durante al menos media hora antes de cortar en rebanadas.",
                "Variaciones: también se puede rellenar con crema pastelera o con helado decorando con crema batida por encima."
            ],
            "teacher_notes": [],
            "notes": ["Receta de Edith's Kitchen."]
        }
    },
    {
        "file": "250_1.json",
        "cluster": "250#1",
        "kind": "recipe",
        "source_refs": ["250#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Crepas de polenta con pollo y brócoli",
            "category": "Platos principales",
            "tags": ["crepas saladas", "polenta", "pollo", "brócoli", "salsa blanca", "queso cheddar", "Edith's Kitchen"],
            "servings": "6-8 porciones",
            "prep_time": "30 min",
            "cook_time": "25 min",
            "temperature": "350°F (175°C)",
            "ingredient_groups": [
                {
                    "name": "Crepas de polenta",
                    "items": [
                        "1/4 Taza de polenta (harina cornmeal amarilla)",
                        "1/2 Taza de agua caliente",
                        "1 Taza de leche tibia",
                        "2 Huevos enteros",
                        "1/2 a 3/4 Taza de harina de trigo cernida",
                        "1 Cucharada de mantequilla derretida o aceite vegetal",
                        "Sal y pimienta al gusto"
                    ]
                },
                {
                    "name": "Relleno de pollo y brócoli",
                    "items": [
                        "1 1/2 Tazas de pechuga de pollo cocida y desmenuzada",
                        "1 Taza de brócoli cocido al dente y picado",
                        "1 Cebolla finamente picada",
                        "2 Dientes de ajo picados"
                    ]
                },
                {
                    "name": "Salsa blanca y gratinado",
                    "items": [
                        "1 Cucharada de mantequilla",
                        "1 Cucharada de harina de trigo",
                        "1 Taza de leche tibia",
                        "Un toque de vino blanco",
                        "1 Taza de queso cheddar rallado (dividido)"
                    ]
                }
            ],
            "steps": [
                "Para la masa de crepas: colocar la polenta en un tazón con la media taza de agua caliente y dejar reposar durante 10 minutos para que el grano se ablande.",
                "Añadir la leche tibia, los huevos, la harina cernida, la mantequilla derretida, sal y pimienta. Batir bien hasta obtener un batido liso.",
                "Cocinar las crepas en una sartén ligeramente engrasada con mantequilla, dorando ambos lados con cuidado.",
                "Para la salsa blanca: derretir la mantequilla en una ollita, agregar la cucharada de harina y cocinar 1 minuto (roux); verter la leche revolviendo hasta espesar, añadir un chorrito de vino blanco y un tercio del queso cheddar rallado.",
                "En un tazón, sofreír la cebolla y el ajo, mezclar con el pollo desmenuzado, el brócoli picado y un par de cucharadas de salsa blanca.",
                "Rellenar cada crepa con la preparación de pollo y brócoli, enrollar y acomodar en una fuente refractaria (pyrex).",
                "Cubrir las crepas con el resto de la salsa blanca y espolvorear el queso cheddar restante.",
                "Hornear a 350°F por 10 a 15 minutos hasta que el queso esté derretido y burbujeante."
            ],
            "teacher_notes": [],
            "notes": ["Receta de Edith's Kitchen."]
        }
    },
    {
        "file": "251_1.json",
        "cluster": "251#1",
        "kind": "recipe",
        "source_refs": ["251#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Masa de pie dulce",
            "category": "Básicos y rellenos",
            "tags": ["masa básica", "pie dulce", "repostería", "tartas", "Edith's Kitchen"],
            "servings": "1 molde de pie de 9 pulgadas (23 cm)",
            "prep_time": "20 min (más 1 hora de reposo)",
            "cook_time": "0 min (cruda)",
            "temperature": "Refrigeración / 375°F para hornear a ciegas",
            "ingredient_groups": [
                {
                    "name": "Ingredientes de la masa",
                    "items": [
                        "2 Tazas de harina de trigo",
                        "1/2 Taza de mantequilla bien fría cortada en dados",
                        "4 Yemas de huevo",
                        "5 Cucharadas de azúcar",
                        "1/2 Cucharadita de sal",
                        "6 a 7 Cucharadas de agua bien fría (congelada)"
                    ]
                }
            ],
            "steps": [
                "Colocar la harina cernida sobre la mesa de trabajo o en un tazón amplio formando una fuente o volcán.",
                "En el centro, colocar los dados de mantequilla fría, las 4 yemas de huevo, el azúcar, la sal y las cucharadas de agua helada.",
                "Con la punta de los dedos o un estribo cortador de masa, ir integrando los ingredientes sin amasar demasiado, hasta formar una masa compacta y suave pero quebradiza.",
                "Formar un disco, envolverlo en plástico de cocina (film) y dejar reposar en el refrigerador durante al menos 1 hora.",
                "Extender en frío con rodillo sobre mesa enharinada y forrar el molde de pie.",
                "Rellenar y hornear según la receta elegida."
            ],
            "teacher_notes": [],
            "notes": [
                "Receta de Edith's Kitchen. La clave para una textura hojaldrada y quebradiza es mantener la mantequilla muy fría y no sobreamasar."
            ]
        }
    },
    {
        "file": "253_1.json",
        "cluster": "253#1",
        "kind": "recipe",
        "source_refs": ["253#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Fusilli con salsa de chile pimiento",
            "category": "Platos principales",
            "tags": ["pastas", "fusilli", "chile pimiento", "queso cheddar", "queso mozzarella", "leche evaporada", "Edith's Kitchen"],
            "servings": "6-8 porciones",
            "prep_time": "15 min",
            "cook_time": "25 min",
            "temperature": "350°F (175°C)",
            "ingredient_groups": [
                {
                    "name": "Pasta",
                    "items": [
                        "1 Libra de pasta fusilli (tornillos)",
                        "Agua abundante con sal y un chorrito de aceite para hervir"
                    ]
                },
                {
                    "name": "Salsa de pimiento y quesos",
                    "items": [
                        "2 Latas de chile pimiento morrón",
                        "1 Lata de leche evaporada",
                        "4 Onzas de queso cheddar rallado",
                        "4 Onzas de queso mozzarella rallado",
                        "2 Onzas de margarina o mantequilla",
                        "Paprika (pimentón en polvo) al gusto",
                        "Sal al gusto"
                    ]
                }
            ],
            "steps": [
                "Cocer los tornillos fusilli en abundante agua hirviendo con sal y un toque de aceite hasta que queden al dente; colar y escurrir.",
                "Licuar las 2 latas de chile pimiento morrón con la lata de leche evaporada hasta obtener una mezcla fina y homogénea.",
                "En un recipiente a baño María, derretir las 2 onzas de margarina junto con el queso cheddar y el queso mozzarella.",
                "Cuando los quesos se hayan fundido suavemente, añadir la mezcla licuada de pimientos y leche evaporada.",
                "Sazonar con paprika y sal al gusto, mezclando hasta que todo esté perfectamente integrado y cremoso.",
                "Engrasar un pyrex o fuente para horno, colocar la pasta cocida y bañar con la salsa de pimientos y quesos.",
                "Hornear a 350°F durante unos 15 a 20 minutos hasta que la salsa rompa hervor y dore ligeramente la superficie."
            ],
            "teacher_notes": [],
            "notes": ["Receta de Edith's Kitchen."]
        }
    },
    {
        "file": "254_1.json",
        "cluster": "254#1",
        "kind": "recipe",
        "source_refs": ["254#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Masa básica de frituras dulces",
            "category": "Básicos y rellenos",
            "tags": ["masa básica", "rebozado", "frituras", "buñuelos", "postres", "Edith's Kitchen"],
            "servings": "Para rebozar fruta de 6 a 8 porciones",
            "prep_time": "15 min",
            "cook_time": "10 min",
            "temperature": "Fritura profunda",
            "ingredient_groups": [
                {
                    "name": "Ingredientes de la pasta",
                    "items": [
                        "3/4 Taza de harina de trigo",
                        "1 Cucharada de azúcar",
                        "1 Cucharada de mantequilla derretida",
                        "1 Taza de agua tibia",
                        "1 Pizca de sal",
                        "1 Huevo (separada la yema de la clara)",
                        "Aceite vegetal abundante para freír"
                    ]
                }
            ],
            "steps": [
                "Cernir juntos la harina y el azúcar en un tazón.",
                "Añadir la mantequilla derretida y el agua tibia poco a poco, batiendo hasta formar una pasta suave y homogénea.",
                "Agregar la yema de huevo y la pizca de sal, integrando bien.",
                "En un tazón aparte, batir la clara de huevo a punto de nieve firme.",
                "Incorporar la clara batida a la masa con movimientos suaves y envolventes para airear la pasta.",
                "Sumergir y forrar por completo trozos de fruta (como rodajas de manzana o banano) en esta pasta.",
                "Freír de inmediato en abundante aceite bien caliente hasta que inflen y doren parejamente por ambos lados.",
                "Escurrir sobre papel absorbente y servir calientes."
            ],
            "teacher_notes": [],
            "notes": ["Receta de Edith's Kitchen."]
        }
    },
    {
        "file": "255_1.json",
        "cluster": "255#1",
        "kind": "recipe",
        "source_refs": ["255#1"],
        "source_hash": "manual",
        "recipe": {
            "title": "Frituras de manzana o banano",
            "category": "Postres y pasteles",
            "tags": ["frituras", "manzana", "banano", "masa choux", "postres", "canela", "Edith's Kitchen"],
            "servings": "6-8 porciones",
            "prep_time": "20 min",
            "cook_time": "15 min",
            "temperature": "Fritura profunda",
            "ingredient_groups": [
                {
                    "name": "Ingredientes",
                    "items": [
                        "1 Receta de masa choux preparada",
                        "3 Manzanas o bananos tajados en rebanadas uniformes",
                        "2 Cucharadas de azúcar (para macerar fruta)",
                        "Unas gotas de jugo de limón",
                        "Aceite vegetal abundante para freír en grasa profunda",
                        "Azúcar con canela molida para espolvorear al servir"
                    ]
                }
            ],
            "steps": [
                "Pelar y tajar las manzanas o bananos en rodajas parejas.",
                "Colocar las tajadas de fruta en un plato hondo y macerarlas durante 10 minutos con el azúcar y unas gotas de jugo de limón.",
                "Tener lista la masa choux.",
                "Envolver cada rebanada de fruta macerada sumergiéndola en la masa choux para que quede bien cubierta.",
                "Dejar caer con cuidado las piezas cubiertas en abundante aceite caliente (fritura profunda).",
                "Freír hasta que la masa se infle, quede hueca y adquiera un color dorado parejo y apetitoso.",
                "Retirar con espumadera, escurrir sobre papel absorbente y espolvorear de inmediato con azúcar y canela antes de servir calientes."
            ],
            "teacher_notes": [],
            "notes": ["Receta de Edith's Kitchen."]
        }
    }
]

for r in new_recipes:
    file_path = RECIPES_DIR / r["file"]
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(r, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Created {file_path}")

print("Batch 29 recipes written successfully.")
