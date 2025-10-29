<script setup>
import {ref} from 'vue';
const titulo = 'Estudiantes Para Desarrolladores Full Stack';
const fecha = 'Enero 2025 - Enero 2027';
const experiencias = ref([
    {id: 1 , src: '/src/assets/estudiante.png', parrafo : 'Primere Semestre con nuevas rutas de conocimiento en el ambito teccnologico...' },
    {id: 2 , src: '/src/assets/estudiante.png', parrafo : 'Segundo semestre asentando conocimientos previos, mas conceptos nuevos aplicados de la maneera mas profesional posible...' },
    {id: 3 , src: '/src/assets/estudiante.png', parrafo : 'Esperando tercer semestre con ansias...' },
    {id: 4 , src: '/src/assets/estudiante.png', parrafo : 'Esperando cuarto semestre con ansias...' },
])
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
    background-color: rgb(28, 41, 52);
    border-radius: 15px;
}

.titulo{
    font-size: 1.5rem;
    color: coral;
}

.fecha{
    font-size: 1rem;
    color: burlywood;
    margin-bottom: 1rem;
}

.listado{
    display: flex;
    flex-direction: column;
}

.item{
    align-items: center;
    display: flex;
    padding: 1rem;
    gap: 1.5rem;
}
</style>