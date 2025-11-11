<script setup>
//              IMPORTACIONES
import imagenSrc from '/src/assets/proyecto.jpg';
import { ref } from 'vue';

const proyectos = ref([
  {
    id: '1',
    titulo: 'Primer Semestre',
    descripcion: 'Portafolio Primer semestre Utnenes',
    linkPagina: 'https://otarkebadze.github.io/utnenes-portfolio',
    img: imagenSrc
  },
  {
    id: '2',
    titulo: 'Segundo Semestre',
    descripcion: 'Portafolio Segundo Semestre Utnenes',
    linkPagina: '#blank',
    img: imagenSrc
  }
]);
</script>

<template>
  <div class="galeria">
    <div class="proyecto" v-for="proyecto in proyectos" :key="proyecto.id">
      <div class="proyecto-img-container">
        <img :src="proyecto.img" :alt="proyecto.titulo" />
        <div class="proyecto-overlay"></div>
      </div>

      <div class="proyecto-info">
        <h3>{{ proyecto.titulo }}</h3>
        <p>{{ proyecto.descripcion }}</p>
        <div class="proyecto-links">
          <a
            :href="proyecto.linkPagina"
            class="btn-ver-mas"
            target="_blank"
            rel="noopener noreferrer"
          >
            Ver Proyecto
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.galeria {
  width: 100%;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  padding: 2rem;
  background: linear-gradient(135deg, #e9e6ff, #d6f0ff);
}

.proyecto {
  display: flex;
  flex-direction: column;
  border-radius: 1rem;
  overflow: hidden;
  background: #ffffff;
  box-shadow: 0 4px 20px rgba(100, 100, 255, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.proyecto:hover {
  transform: translateY(-8px);
  box-shadow: 0 8px 25px rgba(100, 100, 255, 0.25);
}

.proyecto-img-container {
  position: relative;
  height: 200px;
  overflow: hidden;
  border-bottom: 3px solid #b388ff;
}

.proyecto img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.proyecto:hover img {
  transform: scale(1.1);
}

.proyecto-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to bottom, transparent, rgba(0, 0, 0, 0.3));
  opacity: 0.4;
  transition: opacity 0.4s ease;
}

.proyecto:hover .proyecto-overlay {
  opacity: 0.2;
}

.proyecto-info {
  padding: 1.5rem;
  text-align: center;
}

.proyecto-info h3 {
  color: #5e35b1;
  font-size: 1.4rem;
  margin-bottom: 0.5rem;
}

.proyecto-info p {
  color: #555;
  font-size: 1rem;
  margin-bottom: 1.5rem;
  line-height: 1.5;
}

.proyecto-links {
  display: flex;
  justify-content: center;
}

.btn-ver-mas {
  background: linear-gradient(135deg, #7e57c2, #64b5f6);
  color: #fff;
  padding: 0.8rem 1.6rem;
  border-radius: 50px;
  text-decoration: none;
  font-weight: 600;
  letter-spacing: 0.5px;
  transition: all 0.3s ease;
}

.btn-ver-mas:hover {
  background: linear-gradient(135deg, #9575cd, #81d4fa);
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(126, 87, 194, 0.3);
}

@media (max-width: 768px) {
  .galeria {
    grid-template-columns: 1fr;
    padding: 1rem;
  }

  .proyecto-info h3 {
    font-size: 1.2rem;
  }

  .btn-ver-mas {
    padding: 0.7rem 1.3rem;
  }
}
</style>
