<script setup>
import {ref} from 'vue';

const intereses= ref(
    [
    'Apasionados del biohacking y la tecnología del bienestar, porque cada herramienta que mejora mi cuerpo o mente se convierte en un power-up dentro de mi sistema de entrenamiento integral.',
    'Crear y resolver juegos mentales con programación, donde cada desafío lógico se transforma en un logro desbloqueado en mi radar cognitivo.',
    'Pasion pór lo fitness gamificado con tecnología, ya que cada entrenamiento exitoso representa una subida de nivel en mi algoritmo físico-emocional.',
    'Meditación guiada con enfoque técnico, visualizando cada momento de claridad como un debug emocional en mi sistema operativo personal.',
    'Explorar interfaces cerebro-computadora, donde cada avance representa una conexión directa entre pensamiento y código.',
    'Diseño de rutinas físicas como sistemas modulares, donde cada ejercicio es una función que fortalece mi arquitectura corporal.'
    ]
)

</script>

<template>
  <div class="intereses-contenedor">
    <ul class="contenedor-lista">
        <li class="item" v-for="int in intereses" :key='int'>
            {{  int }} 
        </li>
    </ul>
  </div>
</template>

<style scoped>

.intereses-contenedor{
    display: flex;
    position: relative;
    margin: 0 auto;
    max-width: 85%;
    padding: 1rem;
}

.contenedor-lista{
    list-style-type: none;
    padding: 1rem;
    margin-bottom: .5rem;
    color: var(--vt-c-white-soft);
    font-size: 1.4rem;
    text-shadow: 3px 3px 6px rgba(0, 0, 0, 1);
}

.item {
    margin-bottom: 1rem;
}

@keyframes auroraPulse {
  0% {
    background-position: 0% 50%;
    filter: brightness(1);
  }
  50% {
    background-position: 100% 50%;
    filter: brightness(1.5);
  }
  100% {
    background-position: 0% 50%;
    filter: brightness(1);
  }
}

.item {
  margin-bottom: 1rem;
  padding: 1rem;
  border-radius: 12px;
  background: linear-gradient(120deg, rgba(95, 122, 153, 0.2), rgba(60, 79, 102, 0.1));
  color: #cfd8e3;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.item:hover {
  animation: auroraPulseGray 2s ease-in-out infinite;
  box-shadow: 0 0 20px rgba(95, 122, 153, 0.4);
  transform: scale(1.02);
  cursor: pointer;
}

.item:active {
  animation: none;
  background: linear-gradient(120deg, rgba(255,255,255,0.2), rgba(95,122,153,0.3));
  box-shadow: 0 0 30px rgba(95, 122, 153, 0.6);
  transform: scale(1.05);
}

.intereses-contenedor {
  display: flex;
  position: relative;
  margin: 0 auto;
  max-width: 85%;
  padding: 1rem;
  border: 4px solid;
  border-radius: 20px;
  animation: auroraPulseGray 6s linear infinite;
  box-shadow: 0 0 20px rgba(0, 255, 204, 0.4);
}

@keyframes auroraPulseGray {
  0% {
    background-position: 0% 50%;
    filter: brightness(1);
  }
  50% {
    background-position: 100% 50%;
    filter: brightness(1.3);
  }
  100% {
    background-position: 0% 50%;
    filter: brightness(1);
  }
}
</style>