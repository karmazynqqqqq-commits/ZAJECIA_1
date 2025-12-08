import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_mikolaj():
    """Rysuje prostego Mikołaja za pomocą figur Matplotlib."""

    # 1. Ustawienie figury i osi
    fig, ax = plt.subplots(figsize=(6, 8))
    # Ustaw zakresy osi, żeby Mikołaj był dobrze widoczny
    ax.set_xlim(-5, 5)
    ax.set_ylim(-8, 3)
    ax.set_aspect('equal') # Ważne, żeby koła były okrągłe!
    ax.axis('off') # Ukrycie osi

    # 2. Ciało (czerwony prostokąt)
    body = patches.Rectangle(
        (-2.5, -7), 5, 4, # (x, y), szerokość, wysokość
        facecolor='red',
        edgecolor='black',
        linewidth=2
    )
    ax.add_patch(body)

    # 3. Pasek (czarny prostokąt)
    belt = patches.Rectangle(
        (-3, -3.5), 6, 0.5,
        facecolor='black',
        edgecolor='black'
    )
    ax.add_patch(belt)

    # 4. Klamra paska (żółty/złoty kwadrat)
    buckle = patches.Rectangle(
        (-0.5, -3.4), 1, 0.3,
        facecolor='gold',
        edgecolor='black'
    )
    ax.add_patch(buckle)

    # 5. Głowa (beżowe koło)
    head = patches.Circle(
        (0, -1), 1.5, # (x, y) środek, promień
        facecolor='#f0d9c5', # Beżowy kolor skóry
        edgecolor='black',
        linewidth=2
    )
    ax.add_patch(head)

    # 6. Czapka (czerwony trójkąt)
    hat = patches.Polygon(
        [(-2, -1.2), (2, -1.2), (0, 2.5)], # Wierzchołki
        facecolor='red',
        edgecolor='black',
        linewidth=2
    )
    ax.add_patch(hat)

    # 7. Obszycie czapki (biały prostokąt)
    hat_trim = patches.Rectangle(
        (-2, -1.2), 4, 0.5,
        facecolor='white',
        edgecolor='black'
    )
    ax.add_patch(hat_trim)

    # 8. Pompon (białe koło)
    pom_pom = patches.Circle(
        (0, 2.5), 0.5,
        facecolor='white',
        edgecolor='black',
        linewidth=2
        )
    ax.add_patch(pom_pom)

    # 9. Oczy (czarne koła)
    eye_left = patches.Circle(
        (-0.5, -0.5), 0.1,
        color='black'
    )
    eye_right = patches.Circle(
        (0.5, -0.5), 0.1,
        color='black'
    )
    ax.add_patch(eye_left)
    ax.add_patch(eye_right)

    # 10. Broda (biały elipsa - prostsze niż skomplikowane kształty)
    beard = patches.Ellipse()
        (0, -2.5), 3.5, 3.5, # (x, y) środek,
