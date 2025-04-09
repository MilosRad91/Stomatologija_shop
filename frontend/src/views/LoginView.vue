
<template>
  <section class="h-100 gradient-form" style="background-color: #eee">
    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-xl-10">
          <div class="card rounded-3 text-black">
            <div class="row g-0">
              <div class="col-lg-6">
                <div class="card-body p-md-5 mx-md-4">
                  <div class="text-center">
                    <img
                      src="../images/zubic1.avif"
                      style="width: 185px"
                      alt="logo"
                    />
                    <h4 class="mt-1 mb-5 pb-1">Stomatologija shop</h4>
                  </div>

                  <form>
                    <p>Unesite vase login podatke</p>

                    <div data-mdb-input-init class="form-outline mb-4">
                      <input
                        type="email"
                        id="form2Example11"
                        class="form-control"
                        placeholder="Email address"
                        v-model="email"
                      />
                      <label class="form-label" for="form2Example11"
                        >Email</label
                      >
                    </div>

                    <div data-mdb-input-init class="form-outline mb-4">
                      <input
                        type="password"
                        id="form2Example22"
                        class="form-control"
                        v-model="password"
                      />
                      <label class="form-label" for="form2Example22"
                        >Password</label
                      >
                    </div>

                    <div class="text-center pt-1 mb-5 pb-1">
                      <button
                        data-mdb-button-init
                        data-mdb-ripple-init
                        class="btn btn-primary btn-block fa-lg mb-3 btn-lg"
                        type="button"
                        @click="uloguj_se"
                      >
                        Log in
                      </button>
                    </div>

                    <div
                      class="d-flex align-items-center justify-content-center pb-4"
                    >
                      <p class="mb-0 me-2">Nemate nalog?</p>
                      <router-link to="/register">
                        <button
                          type="button"
                          data-mdb-button-init
                          data-mdb-ripple-init
                          class="btn btn-outline-danger btn-lg"
                        >
                          Otvori nalog
                        </button>
                      </router-link>
                    </div>
                  </form>
                </div>
              </div>
              <div class="col-lg-6 d-flex align-items-center gradient-custom-2">
                <div class="text-white px-3 py-4 p-md-5 mx-md-4">
                  <h4 class="mb-4">Mi smo vise od prodavnice</h4>
                  <p class="small mb-0">
                    Nasa prodavnica je specijalizovana za prodaju stomatoloskog
                    materijala i opreme, kako u zemlji tako i u inostranstvu.
                    Dugogodisnja tradicija i iskustvo nasih prodavaca pomoci ce
                    Vam da pronadjete sve sto Vam je potrebno za svakodnevni
                    rad.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import { RouterLink } from "vue-router";

export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {

    async uloguj_se() {
      if (this.email == "" || this.password == "") {
        return this.$toast.error("Morate popuniti sva polja da biste se ulogovali")
      }
      try {
        const response = await axios.post("http://127.0.0.1:5000/login", {
          email: this.email,
          password: this.password,
        });

        const vrstaKorisnika = response.data.korisnik;
        const korpa = response.data.korpa;
        console.log(vrstaKorisnika.naziv);

        // sessionStorage.setItem("vrsta_korisnika", vrstaKorisnika.naziv);
        // sessionStorage.setItem("korisnik_id", vrstaKorisnika.id)
        if (vrstaKorisnika.naziv === "kupac") {
          sessionStorage.setItem('korisnik', JSON.stringify({ vrsta_korisnika: vrstaKorisnika.naziv, korisnik_id: vrstaKorisnika.idKorisnici, korpa_status:korpa.status, korpa_id: korpa.idKorpa }));
        }
        else {
          sessionStorage.setItem('korisnik', JSON.stringify({ vrsta_korisnika: vrstaKorisnika.naziv, korisnik_id: vrstaKorisnika.idKorisnici}));
        }
        // Preusmeravanje na odgovarajući ShopView
        if (vrstaKorisnika.naziv === "kupac") {
          this.$router.push({ name: "shop-kupac" });
          this.$toast.success("Uspesno ste se ulogovali")
        } else if (vrstaKorisnika.naziv === "prodavac") {
          this.$router.push({ name: "shop-prodavac" });
          this.$toast.success("Uspesno ste se ulogovali")
        } else if (vrstaKorisnika.naziv === "admin") {
          this.$router.push({ name: "shop-admin" });
          this.$toast.success("Uspesno ste se ulogovali")
        }
      } catch (error) {
        this.$toast.error("Neadekvatni podaci za prijavu")
      }
    },
  },

  // mounted() {
  //   this.dohvati_sve_korisnike();
  // },
};
</script>

<style scoped>
.gradient-custom-2 {
  
  background: #fccb90;

  
  background: -webkit-linear-gradient(
    to right,
    #ee7724,
    #d8363a,
    #dd3675,
    #b44593
  );

  background: linear-gradient(to right, #ee7724, #d8363a, #dd3675, #b44593);
}

@media (min-width: 768px) {
  .gradient-form {
    height: 100vh !important;
  }
}
@media (min-width: 769px) {
  .gradient-custom-2 {
    border-top-right-radius: 0.3rem;
    border-bottom-right-radius: 0.3rem;
  }
}
</style>
