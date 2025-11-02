<script setup>
//              IMPORTACIONES
import imagenSrc from '/src/assets/proyecto.jpg';
import {ref} from 'vue';

const proyectos = ref([
    {id:'1' , titulo:'Primer Semestre' , descripcion :'Portafolio Primer semestre Utnenes',linkPagina:'https://otarkebadze.github.io/utnenes-portfolio', linkGithub:'https://github.com/OtarKebadze/utnenes-portfolio', img:imagenSrc},
    {id:'2' , titulo:'Segundo Semestre' , descripcion :'Portafolio Segundo Semestre Utnenes',linkPagina:'#blank', linkGithub:'#blank', img:imagenSrc},
])
</script>

<template>
  <div class="galeria" >
    <div class="proyecto" v-for='proyecto in proyectos' :key="proyecto.id">
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
            rel="noopener noreferrer">
            Ver Proyecto
          </a>
          <a
            :href="proyecto.linkGithub"
            class="github-link"
            target="_blank"
            rel="noopener noreferrer">
            <span>Ver código</span>
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
  background: var(--color-background);
}

.proyecto {
  display: flex;
  flex-direction: column;
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius-lg);
  overflow: hidden;
  background: var(--color-background-soft);
  transition: all var(--transition-smooth);
  position: relative;
}

.proyecto:hover {
  transform: translateY(-5px);
  border-color: var(--color-primary);
  box-shadow: var(--shadow-glow);
}

.proyecto-img-container {
  position: relative;
  overflow: hidden;
  height: 200px;
}

.proyecto img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform var(--transition-smooth);
}

.proyecto:hover img {
  transform: scale(1.05);
}

.proyecto-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, transparent 0%, var(--color-background) 100%);
  opacity: 0.3;
  transition: opacity var(--transition-smooth);
}

.proyecto:hover .proyecto-overlay {
  opacity: 0.1;
}

.proyecto-info {
  padding: 1.5rem;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.proyecto-info h3 {
  margin: 0 0 0.5rem 0;
  font-size: 1.3em;
  color: var(--color-heading);
  font-weight: 600;
}

.proyecto-info p {
  color: var(--color-text);
  margin: 0 0 1.5rem 0;
  line-height: 1.5;
  flex-grow: 1;
}

.proyecto-links {
  display: flex;
  gap: 1rem;
  margin-top: auto;
}

.btn-ver-mas {
  background: var(--color-primary);
  color: var(--color-background);
  padding: 0.75rem 1.5rem;
  border-radius: var(--border-radius);
  text-decoration: none;
  font-weight: 600;
  transition: all var(--transition-smooth);
  flex: 1;
  text-align: center;
  border: 2px solid var(--color-primary);
}

.btn-ver-mas:hover {
  background: transparent;
  color: var(--color-primary);
  transform: translateY(-2px);
}

.github-link {
  background: transparent;
  color: var(--color-text);
  padding: 0.75rem 1.5rem;
  border-radius: var(--border-radius);
  text-decoration: none;
  font-weight: 600;
  transition: all var(--transition-smooth);
  flex: 1;
  text-align: center;
  border: 2px solid var(--color-border);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.github-link:hover {
  border-color: var(--color-primary);
  color: var(--color-primary);
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .galeria {
    grid-template-columns: 1fr;
    padding: 1rem;
    gap: 1.5rem;
  }
  
  .proyecto-links {
    flex-direction: column;
  }
}
</style>