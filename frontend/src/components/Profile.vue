<template>

    <div class="container my-5">
      <div class="row">
        <!-- Profilna slika i osnovne informacije -->
        <div class="col-md-4">
          <div class="profile-header text-center">
            <p>Korisničko ime</p>
            <h2>@{{ korisnik.username }}</h2>
          </div>
        </div>
  
        <!-- Profilni podaci -->
        <div class="col-md-8">
          <div class="profile-card">
            <h3>Ostali podaci</h3>
            <hr>
            <div class="profile-info">
              <label for="email">Email:</label>
              <p id="email">{{ korisnik.email }}</p>
            </div>
  
            <div class="profile-info">
              <label for="datum_rodjenja">Godina Rođenja:</label>
              <p id="datum_rodjenja">{{ korisnik.godina_rodjenja }}</p>
            </div>
  
            <div class="profile-info">
              <label for="zanimanje">Stanje na računu:</label>
              <p id="zanimanje">{{ korisnik.trenutno_stanje_novca }} din</p>
            </div>
            <div class="d-flex justify-content-between">
              <button class="btn btn-primary">Uredi Profil</button>
              <router-link :to="'/shop/' + vrsta_korisnika"
                ><button class="btn btn-danger">Nazad</button></router-link
              >
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'Profile',
    data() {
      return {
        korisnik: [],
        vrsta_korisnika: null
      }
    },
    methods: {
      async dohvati_korisnika() {
        const get_korisnik = sessionStorage.getItem('korisnik');
        const ulogovani_korisnik = JSON.parse(get_korisnik)
        this.vrsta_korisnika = ulogovani_korisnik.vrsta_korisnika
        // console.log(ulogovani_korisnik.korisnik_id);
        const response = await axios.post('http://127.0.0.1:5000/korisnik', {
          id_korisnika: ulogovani_korisnik.korisnik_id
        })
  
        this.korisnik = response.data.korisnik
        console.log(this.korisnik);
      }
    },
    mounted() {
      this.dohvati_korisnika()
    },
  };
  </script>
  
  <style scoped>
  .profile-header {
    background-color: #007bff;
    color: white;
    padding: 30px;
    border-radius: 10px 10px 0 0;
  }
  .profile-header h2 {
    margin: 0;
  }
  .profile-img {
    border-radius: 50%;
    border: 5px solid white;
    width: 150px;
    height: 150px;
    object-fit: cover;
  }
  .profile-card {
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    padding: 30px;
    background-color: #fff;
  }
  .profile-info {
    margin-bottom: 20px;
  }
  .profile-info label {
    font-weight: bold;
  }
  .profile-info p {
    margin-bottom: 0;
  }
  .btn-primary {
    width: 48%;
    font-size: 16px;
  }
  
  </style>