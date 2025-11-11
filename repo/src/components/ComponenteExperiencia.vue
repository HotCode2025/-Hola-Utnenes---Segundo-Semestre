<script setup>
    import { ref } from 'vue'

    // 
    // import iconSewing from '../assets/sewing-machine-svgrepo-com.svg'
    // import iconEstudiante from '../assets/estudiante-svgrepo-com.svg'
    import iconSewing from '@/assets/sewing-machine-svgrepo-com.svg'
    import iconEstudiante from '@/assets/estudiante-svgrepo-com.svg'

    const titulo = 'Estudiante para Desarrollador/a Full Stack'
    const fecha = 'Enero 2025 – Enero 2027'

    const experiencia = ref([
        {
            id: 1,
            src: iconSewing,
            parrafo:
                'Profesor de robotica / Taller propio (2020 – Actualidad). Confección a medida (alta costura: vestidos de fiesta y trajes formales). Gestión de clientes y pedidos personalizados.'
        },
        {
            id: 2,
            src: iconEstudiante,
            parrafo:
                'Estudiante de Técnico Universitario en Programación – Cohorte 2025 (“Hola UTNenes”) – UTN San Rafael. Desarrollo de proyectos web y móviles.'
        }
    ])
</script>

<template>
    <div>
        <div class="card">
            <h3 class="titulo">{{ titulo }}</h3>
            <p class="fecha">{{ fecha }}</p>

            <ul class="listado" role="list">
                <li class="item" v-for="exp in experiencia" :key="exp.id" role="listitem">
                    <img v-if="exp.src" :src="exp.src" :alt="exp.parrafo" class="icono" />
                    <p class="texto">{{ exp.parrafo }}</p>
                </li>
            </ul>
        </div>
    </div>
</template>

<style scoped>
    .card {
        display: flex;
        flex-direction: column;
        padding: 2rem;
        /* ❌ antes: background-color con tres valores separados por coma
     ✅ ahora: un gradiente suave */
        background: linear-gradient( 135deg, rgba(167, 98, 98, 0.12), rgba(166, 197, 166, 0.12), rgba(159, 159, 187, 0.12) );
        border: 1px solid var(--color-border);
        border-radius: 15px;
        transition: all var(--transition-fast);
    }

        .card:hover {
            border-color: var(--color-border-hover);
            transform: translateY(-2px);
        }

    .titulo {
        font-size: 1.5rem;
        color: coral;
        margin-bottom: 0.5rem;
    }

    .fecha {
        font-size: 1rem;
        color: rosybrown;
        opacity: 0.85;
        margin-bottom: 1rem;
    }

    .listado {
        display: flex;
        flex-direction: column;
        gap: 0.75rem;
        margin: 0;
        padding: 0;
        list-style: none;
    }

    .item {
        display: flex;
        align-items: flex-start;
        padding: 1rem;
        gap: 1rem;
        border-radius: var(--border-radius);
        transition: transform var(--transition-fast), background-color var(--transition-fast);
    }

        .item:hover {
            background-color: var(--color-background-mute);
            transform: translateX(4px);
        }

    .icono {
        width: 45px;
        height: 45px;
        flex: 0 0 45px;
    }

    .texto {
        color: var(--color-text);
        line-height: 1.55;
    }
</style>
