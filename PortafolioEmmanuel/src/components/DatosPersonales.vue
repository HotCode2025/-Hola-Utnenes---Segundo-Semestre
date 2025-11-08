<script setup>
import profile from '../images/profile.jpg';
</script>

<template>
  <section class="perfil fade-up">
    <img :src="profile" alt="Foto de perfil" class="foto" />

    <div class="info">
      <h1>Emmanuel Poletto</h1>
      <h2>Estudiante de la Tecnicatura en Programación - UTN San Rafael</h2>
      <p>
        Soy un estudiante de la Tecnicatura en programación de la UTN de San Rafael, 
        que aspira a recibirse y poder ejercer de esto en un futuro.
      </p>
    </div>
  </section>
</template>

<style scoped>
.perfil {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  background: linear-gradient(180deg, #eaf4ff 0%, #f9fcff 100%);
  padding: 2rem;
  border-radius: 20px;
  max-width: 800px;
  margin: 2rem auto;
  box-shadow: 0 4px 20px rgba(0, 100, 255, 0.1);
  animation: fadeIn 1.2s ease;
}

.foto {
  width: 140px;
  height: 140px;
  border-radius: 50%;
  object-fit: cover;
  box-shadow: 0 0 15px rgba(0, 100, 255, 0.2);
  margin-bottom: 1.5rem;
  transition: transform 0.3s ease;
}

.foto:hover {
  transform: scale(1.05);
}

h1 {
  color: #003366;
  font-size: 1.8rem;
  margin-bottom: 0.5rem;
}

h2 {
  color: #0056b3;
  font-size: 1.1rem;
  margin-bottom: 1rem;
}

p {
  color: #0a2a43;
  line-height: 1.6;
  font-size: 1rem;
  max-width: 600px;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>