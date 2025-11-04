<script setup>
import { ref } from 'vue';
import iconEstudiante from '/src/assets/estudiante.png';

const titulo = 'Estudiantes Para Desarrolladores Full Stack';
const fecha = 'Enero 2025 - Enero 2027';

const experiencias = ref([
    { id: 1, src: iconEstudiante, parrafo: 'Trabajo de chef desde 2012 hasta actualidad, en restaurantes a lo largo del mundo y eventos' },
    { id: 2, src: iconEstudiante, parrafo: 'Estudiante de coderhouse - Fullstack Js (MERN)' },
    { id: 3, src: iconEstudiante, parrafo: 'Pasantias Semillero Quinto Impacto como frontend' },
    { id: 4, src: iconEstudiante, parrafo: 'Estudiando y haciendo proyectos para tectnico en programacion en COHORTE 2025 - ("HOLA UTNENES") - UTN SAN RAFAEL '},
]);
</script>

<template>
  <div>
    <div class="card">
        <h3 class="titulo">{{ titulo.toUpperCase() }}</h3>
        <p class="fecha">{{ fecha }}</p>
        <ul class="listado">
            <li class='item' v-for='exp in experiencias' :key="exp.id">
                <img :src='exp.src' alt="" width="45rem">
                <p>{{ exp.parrafo }}</p>
            </li>
        </ul>
    </div>
  </div>
</template>

<style scoped>
.card{
    display: flex;
    flex-direction: column;
    padding: 2rem;
    background-color: var(--color-background-soft);
    border: 1px solid var(--color-border);
    border-radius: var(--border-radius);
    transition: all var(--transition-fast);
}

.card:hover{
    border-color: var(--color-border-hover);
    transform: translateY(-2px);
}

.titulo{
    font-size: 1.5rem;
    color: var(--color-heading);
    margin-bottom: 0.5rem;
}

.fecha{
    font-size: 1rem;
    color: var(--color-text);
    opacity: 0.8;
    margin-bottom: 1rem;
}

.listado{
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.item{
    display: flex;
    align-items: center;
    padding: 1rem;
    gap: 1.5rem;
    background-color: var(--color-background-mute);
    border-radius: var(--border-radius);
    transition: all var(--transition-fast);
}

.item:hover{
    background-color: var(--color-border);
    transform: translateX(4px);
}
</style>