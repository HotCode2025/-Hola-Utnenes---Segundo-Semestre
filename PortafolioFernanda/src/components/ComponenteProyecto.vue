<script setup>
import imagenSrc from '/src/assets/modacode.png'
import { ref } from 'vue'

const proyectos = ref([
  { id: '1', titulo: 'ModaCode', descripcion: 'Plataforma para modistas', linkPagina: 'https://modacode.ar', linkGithub: 'https://github.com/ferdiaz9/moda-code', img: imagenSrc }
])
</script>

<template>
  <div class="galeria">
    <div class="proyecto" v-for="p in proyectos" :key="p.id">
      <div class="proyecto-img-container">
        <img :src="p.img" :alt="p.titulo" />
      </div>
      <div class="proyecto-info">
        <h3>{{ p.titulo }}</h3>
        <p>{{ p.descripcion }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.galeria {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
  background-color: #fff;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.proyecto {
  width: 280px;
  background: linear-gradient(135deg, #ff69b4 0%, #ffffff 50%, #bfff00 100%);
  border-radius: 16px;
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 0 4px 12px rgba(255, 105, 180, 0.3);
}

.proyecto:hover {
  transform: scale(1.05);
  box-shadow: 0 6px 16px rgba(191, 255, 0, 0.4);
}

.proyecto-img-container {
  width: 100%;
  height: 180px;
  overflow: hidden;
  background-color: #fff;
}

.proyecto-img-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-bottom: 4px solid #bfff00;
}

.proyecto-info {
  padding: 1rem;
  background-color: rgba(255, 255, 255, 0.9);
  text-align: center;
}

.proyecto-info h3 {
  color: #ff69b4;
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}

.proyecto-info p {
  color: #4d4d4d;
  font-size: 0.95rem;
}
</style>