<template>
  <section class="header">
    <img src="@/assets/foto.jpg" alt="Foto de perfil" class="foto" />
    <div class="texto-header">
      <h1>Florencia Martini</h1>
      <p>
        Estudiante de la Tecnicatura en Programación en la UTN FRSR, apasionada por aprender,
        crear soluciones útiles y promover la tecnología al servicio de un futuro sostenible.
      </p>
    </div>
  </section>
</template>

<style scoped>
.header {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  gap: 20px; 
  padding: 20px; 
  margin: 20px auto;
  width: 100%;
  max-width: 1200px; 
  background: linear-gradient(135deg, #d4b3ff, #a866ff, #7200ff);
  color: black;
  border-radius: 20px; 
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.35); 
}

.foto {
  width: 200px; 
  height: 200px;
  border-radius: 50%;
  object-fit: cover;
  border: 4px solid #4b0082;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
}

.texto-header {
  max-width: 800px; 
  text-align: left;
}

h1 {
  font-size: 3rem; 
  margin-bottom: 20px;
  font-weight: bold;
}

p {
  font-size: 1.5rem; 
  line-height: 1.5;
  font-weight: 500;
}

@media (max-width: 1024px) {
  .header {
    gap: 60px;
    padding: 50px 40px;
  }
  .foto {
    width: 160px;
    height: 160px;
  }
  h1 {
    font-size: 2.6rem;
  }
  p {
    font-size: 1.4rem;
  }
}

@media (max-width: 768px) {
  .header {
    flex-direction: column;
    text-align: center;
    gap: 20px;
    padding: 40px 20px;
  }
  .foto {
    width: 140px;
    height: 140px;
  }
  h1 {
    font-size: 2.2rem;
  }
  p {
    font-size: 1.2rem;
  }
}

@media (max-width: 480px) {
  .header {
    padding: 30px 15px;
  }
  .foto {
    width: 100px;
    height: 100px;
  }
  h1 {
    font-size: 1.8rem;
  }
  p {
    font-size: 1rem;
    line-height: 1.4;
  }
}
</style>
