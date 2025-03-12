<template>
  <div class="slika" v-if="get_session_user()">
    <h1>
      Ne mozete pristupiti ovoj stranici jer ste ulogovani kao
      <b>{{ get_session_user() }}.</b>
    </h1>
    <p>
      <router-link :to="'/shop/' + get_session_user()"
        ><button class="btn btn-danger btn-lg ms-5">Nazad</button></router-link
      >
    </p>
    <!-- <img src="../images/stop.png" alt=""> -->
  </div>
  <div v-else-if="flag">
    <h1>Morate se ulogovati da biste pristupili stranici</h1>
    <p>
      <router-link to="/"
        ><button class="btn btn-danger btn-lg ms-5">Nazad</button></router-link
      >
    </p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      flag: false
    }
  },
  methods: {
    get_session_user() {

      const get_korisnik = sessionStorage.getItem("korisnik");
      const korisnik = JSON.parse(get_korisnik);
      if (korisnik == null) {
        this.flag = true
        return null
      }
      return korisnik.vrsta_korisnika;
      
    },
  },
};
</script>

<style scoped>
h1 {
  text-align: center;
  margin-bottom: 100px;
}
.slika {
  background-image: url("../images/stop.png"); /* Putanja do tvoje slike */
  background-size: cover; /* Slika će pokriti ceo ekran */
  background-position: center; /* Centriraj sliku */
  background-attachment: fixed; /* Slika se neće pomerati dok skroluješ */
  height: 100vh; /* Visina je 100% visine ekrana */
  margin: 0;
}
</style>