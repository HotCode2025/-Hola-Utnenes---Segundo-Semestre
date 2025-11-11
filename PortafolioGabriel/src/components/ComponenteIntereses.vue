<!-- Intereses.vue -->
<script setup>
    import { ref } from 'vue'

    const intereses = ref([
        'Astroturismo y astronomía práctica',
        'Astrofotografía y timelapse',
        'Geología y volcanes (Payunia, Malacara)',
        'Turismo y diseño de experiencias',
        'Desarrollo web (Vue, WordPress/Elementor)',
        'Educación STEAM: robótica, IoT y sensores (Arduino/ESP32)',
        'Impresión 3D y prototipado rápido',
        'Gestión de proyectos y mejora continua',
        'Sostenibilidad y turismo responsable',
        'Fotografía y edición (Lightroom)'
    ])
</script>

<template>
    <div class="intereses-contenedor" role="list">
        <h3 class="titulo-intereses">Intereses</h3>
        <ul class="contenedor-lista" aria-label="Lista de intereses">
            <li class="item"
                v-for="int in intereses"
                :key="int"
                role="listitem">
                {{ int }}
            </li>
        </ul>
    </div>
</template>

<style scoped>
    .intereses-contenedor {
        display: flex;
        flex-direction: column;
        position: relative;
        margin: 0 auto;
        max-width: 85%;
        padding: 2rem;
        border: 1px solid var(--color-border);
        border-radius: var(--border-radius-lg);
        background: var(--color-background-soft);
        box-shadow: var(--shadow-glow);
    }

    .titulo-intereses {
        margin: 0 0 1rem 0;
        font-size: 1.25rem;
        color: var(--color-heading);
    }

    .contenedor-lista {
        list-style-type: none;
        padding: 0;
        margin: 0;
        width: 100%;
    }

    .item {
        margin-bottom: 1.5rem;
        padding: 1.5rem;
        border-radius: var(--border-radius);
        background: var(--color-background-mute);
        color: var(--color-text);
        font-size: 1.1rem;
        line-height: 1.6;
        border: 1px solid transparent;
        transition: all var(--transition-smooth);
        position: relative;
        overflow: hidden;
    }

        .item::before {
            content: "";
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, var(--color-primary), transparent);
            opacity: 0.1;
            transition: left 0.6s ease;
        }

        .item:hover {
            transform: translateY(-3px);
            border-color: var(--color-primary);
            box-shadow: 0 8px 25px rgba(163, 230, 53, 0.15);
            animation: glitch 0.3s ease;
        }

            .item:hover::before {
                left: 100%;
            }

        .item:active {
            transform: translateY(-1px);
            transition: transform 0.1s ease;
        }

        .item:last-child {
            margin-bottom: 0;
        }

    @keyframes glitch {
        0% {
            transform: translate(0);
        }

        20% {
            transform: translate(-2px, 2px);
        }

        40% {
            transform: translate(-2px, -2px);
        }

        60% {
            transform: translate(2px, 2px);
        }

        80% {
            transform: translate(2px, -2px);
        }

        100% {
            transform: translate(0);
        }
    }

    @media (max-width: 768px) {
        .intereses-contenedor {
            max-width: 95%;
            padding: 1rem;
        }

        .item {
            padding: 1rem;
            font-size: 1rem;
        }
    }
</style>
