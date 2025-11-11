<!-- LineaTiempoEducacion.vue -->
<script setup>
    import { ref } from "vue";

    // Paleta para la pastilla de fecha (rota por índice)
    const fechaColor = ref([
        { color: "#41516c" },
        { color: "#e24a68" },
        { color: "#452452" },
        { color: "#41c49c" },
    ]);

    // Datos de educación (ajustá lo que corresponda)
    const educacion = ref([
        {
            fecha: "2025 – 2027",
            titulo: "Técnico Universitario en Programación (UTN – FRSR)",
            descripcion:
                "Cursada orientada a desarrollo de aplicaciones (Java, C#, bases de datos, POO, estructuras, web). Proyectos: TP WinForms + Access, portfolio Vue.",
        },
        {
            fecha: "2024 – Actualidad",
            titulo: "Tecnicatura en Análisis de Sistemas (IES21)",
            descripcion:
                "Análisis, modelado de sistemas, SQL, POO, prácticas con metodologías y reporting.",
        },
        {
            fecha: "2016 – 2018",
            titulo: "Técnico en Turismo y Hotelería",
            descripcion:
                "Gestión de servicios turísticos, coordinación de grupos, operaciones en campo (Payunia, Malargüe), seguridad y atención.",
        },
        {
            fecha: "Cursos y Certificaciones",
            titulo: "WordPress/Elementor • IoT (Arduino/ESP32) • Impresión 3D",
            descripcion:
                "Integración de tecnología en turismo/STEAM, astrofotografía, maquetas solares e instrumentación básica.",
        },
    ]);
</script>

<template>
    <div class="timeline">
        <ul role="list">
            <li v-for="(item, index) in educacion"
                :key="index"
                :style="{ '--fecha-color': fechaColor[index % fechaColor.length].color }"
                role="listitem">
                <div class="fecha">{{ item.fecha }}</div>
                <h3 class="title">{{ item.titulo }}</h3>
                <div class="descripcion">{{ item.descripcion }}</div>
            </li>
        </ul>
        <p class="credits">
            <!-- opcional: créditos/nota -->
        </p>
    </div>
</template>

<style scoped>
    @import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap");

    .timeline {
        font-family: "Poppins", system-ui, Arial, sans-serif;
        color: var(--color-text);
        background-color: transparent;
        padding-block: 1rem;
    }

    ul {
        --col-gap: 2rem;
        --row-gap: 2rem;
        --line-w: 0.25rem;
        display: grid;
        grid-template-columns: var(--line-w) 1fr;
        grid-auto-columns: max-content;
        column-gap: var(--col-gap);
        list-style: none;
        width: min(60rem, 90%);
        margin-inline: auto;
        margin-top: 2rem;
    }

        ul::before {
            content: "";
            grid-column: 1;
            grid-row: 1 / span 20;
            background: var(--color-border);
            border-radius: calc(var(--line-w) / 2);
        }

        ul li:not(:last-child) {
            margin-bottom: var(--row-gap);
        }

        ul li {
            grid-column: 2;
            --inlinerP: 1.5rem;
            margin-inline: var(--inlinerP);
            grid-row: span 2;
            display: grid;
            grid-template-rows: min-content min-content min-content;
        }

            ul li .fecha {
                --dateH: 3rem;
                height: var(--dateH);
                margin-inline: calc(var(--inlinerP) * -1);
                text-align: center;
                background-color: var(--fecha-color); /* ← usa color por ítem */
                color: var(--color-background);
                font-size: 1.05rem;
                font-weight: 700;
                display: grid;
                place-content: center;
                position: relative;
                border-radius: calc(var(--dateH) / 2) 0 0 calc(var(--dateH) / 2);
            }

                ul li .fecha::before {
                    content: "";
                    width: var(--inlinerP);
                    height: var(--inlinerP);
                    background: var(--fecha-color); /* ← mismo color */
                    position: absolute;
                    top: 100%;
                    clip-path: polygon(0 0, 100% 0, 0 100%);
                    right: 0;
                }

                ul li .fecha::after {
                    content: "";
                    position: absolute;
                    width: 1rem;
                    height: 1rem;
                    background: var(--color-background);
                    border: 0.3rem solid var(--fecha-color); /* ← mismo color */
                    border-radius: 50%;
                    top: 50%;
                    transform: translate(50%, -50%);
                    right: calc(100% + var(--col-gap) + var(--line-w) / 2);
                }

            ul li .title,
            ul li .descripcion {
                background: var(--color-background-soft);
                position: relative;
                padding-inline: 1.5rem;
                border-radius: 0.5rem;
            }

            ul li .title {
                overflow: hidden;
                padding-block-start: 1.25rem;
                padding-block-end: 0.85rem;
                font-weight: 600;
                color: var(--color-heading);
            }

            ul li .descripcion {
                padding-block-end: 1.25rem;
                font-weight: 300;
                color: var(--color-text);
            }

                ul li .title::before,
                ul li .descripcion::before {
                    content: "";
                    position: absolute;
                    width: 90%;
                    height: 0.5rem;
                    background: var(--color-border);
                    left: 50%;
                    border-radius: 50%;
                    filter: blur(4px);
                    transform: translate(-50%, 50%);
                }

            ul li .title::before {
                bottom: calc(100% + 0.125rem);
            }

            ul li .descripcion::before {
                z-index: -1;
                bottom: 0.25rem;
            }

    @media (min-width: 40rem) {
        ul {
            grid-template-columns: 1fr var(--line-w) 1fr;
        }

            ul::before {
                grid-column: 2;
            }

            ul li:nth-child(odd) {
                grid-column: 1;
            }

            ul li:nth-child(even) {
                grid-column: 3;
            }

            ul li:nth-child(2) {
                grid-row: 2/4;
            }

            ul li:nth-child(odd) .fecha {
                border-radius: 0 calc(var(--dateH) / 2) calc(var(--dateH) / 2) 0;
            }

                ul li:nth-child(odd) .fecha::before {
                    left: 0;
                    right: auto;
                    clip-path: polygon(100% 0, 100% 100%, 0 0);
                }

                ul li:nth-child(odd) .fecha::after {
                    left: calc(100% + var(--col-gap) + var(--line-w) / 2);
                    right: auto;
                    transform: translate(-50%, -50%);
                }
    }

    .credits {
        margin-top: 1rem;
        text-align: center;
    }

        .credits a {
            color: var(--color-primary);
        }

            .credits a:hover {
                color: var(--color-hover);
            }
</style>
