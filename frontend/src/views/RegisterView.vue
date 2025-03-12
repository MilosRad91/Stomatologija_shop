

<template>
  <section class="vh-100 gradient-custom">
    <div class="container py-5 h-100">
      <div class="row justify-content-center align-items-center h-100">
        <div class="col-12 col-lg-9 col-xl-7">
          <div
            class="card shadow-2-strong card-registration"
            style="border-radius: 15px"
          >
            <div class="card-body p-4 p-md-5">
              <h3 class="mb-4 pb-2 pb-md-0 mb-md-5">Registruj se</h3>
              <form @submit.prevent="registracija_korisnik">
                <div class="row">
                  <div class="col-md-6 mb-4">
                    <div data-mdb-input-init class="form-outline">
                      <input
                        type="text"
                        id="username"
                        class="form-control form-control-lg"
                        v-model="korisnik.username"
                      />
                      <label class="form-label" for="firstName"
                        >Korisnicko ime</label
                      >
                    </div>
                  </div>
                  <div class="col-md-6 mb-4">
                    <div data-mdb-input-init class="form-outline">
                      <input
                        type="password"
                        id="password"
                        class="form-control form-control-lg"
                        v-model="korisnik.password"
                      />
                      <label class="form-label" for="lastName">Sifra</label>
                    </div>
                  </div>
                </div>

                <div class="row">
                  <div class="col-md-6 mb-4 d-flex align-items-center">
                    <div
                      data-mdb-input-init
                      class="form-outline datepicker w-100"
                    >
                      <input
                        type="number"
                        class="form-control form-control-lg"
                        id="godina_rodjenja"
                        v-model="korisnik.godina_rodjenja"
                      />
                      <label for="birthdayDate" class="form-label"
                        >Godina rodjenja</label
                      >
                    </div>
                  </div>
                </div>

                <div class="row">
                  <div class="col-md-6 mb-4 pb-2">
                    <div data-mdb-input-init class="form-outline">
                      <input
                        type="email"
                        id="emailAddress"
                        class="form-control form-control-lg"
                        v-model="korisnik.email"
                      />
                      <label class="form-label" for="emailAddress">Email</label>
                      {{ korisnik.email }}
                    </div>
                  </div>
                  <div class="col-md-6 mb-4 pb-2">
                    <div data-mdb-input-init class="form-outline">
                      <input
                        type="number"
                        id="trenutno_stanje_novca"
                        class="form-control form-control-lg"
                        v-model="korisnik.trenutno_stanje_novca"
                      />
                      <label class="form-label" for="phoneNumber"
                        >Koliko novca zelite da uplatite?</label
                      >
                      {{ korisnik.trenutno_stanje_novca }}
                    </div>
                  </div>
                </div>

                <div class="row">
                  <div class="col-12">
                    <label for="">Registrujem se kao:</label><br />
                    <select
                      class="select form-control-lg"
                      v-model="korisnik.vrsta_korisnika_id"
                    >
                      <option value="a" disabled>Izaberite opciju</option>
                      <option v-for="k in uniqueKorisnici" :key="k.id" :value="k.id">
                        {{ k.naziv }}
                      </option>
                    </select>
                  </div>
                </div>
                <div class="mt-4 pt-2">
                  <button
                    data-mdb-ripple-init
                    class="btn btn-primary btn-lg"
                    type="submit"
                  >
                    Registuj se
                  </button>
                  <router-link to="/"
                    ><button class="btn btn-danger btn-lg m-2">
                      Nazad
                    </button></router-link
                  >
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  {{ korisnici }}
</template>



<script>
import axios from "axios";

export default {
  data() {
    return {
      korisnici: [],
      korisnik: {
        username: "",
        password: "",
        email: "",
        godina_rodjenja: null,
        trenutno_stanje_novca: null,
        vrsta_korisnika_id: null,
      },
    };
  },
  methods: {
    async dohvati_sve_korisnike() {
      const response = await axios.get(
        "http://127.0.0.1:5000/korisnici/sve-vrste"
      );
      this.korisnici = response.data.sve_vrste_korisnika;
    },
    registracija_korisnik() {
      const data = {
        username: this.korisnik.username,
        password: this.korisnik.password,
        email: this.korisnik.email,
        godina_rodjenja: this.korisnik.godina_rodjenja,
        trenutno_stanje_novca: this.korisnik.trenutno_stanje_novca,
        vrsta_korisnika_id: this.korisnik.vrsta_korisnika_id,
      };
      
      if (data.username == "" || data.password == "" || data.email == "" || data.godina_rodjenja == "" || 
      data.trenutno_stanje_novca == "" || data.vrsta_korisnika_id == "") {
        return this.$toast.error("Sva polja moraju biti popunjena")
      }

      axios
        .post("http://localhost:5000/registracija/korisnik", data)
        .then((response) => {
          console.log("Podaci su uspešno poslati:", response);
        })
        .catch((error) => {
          console.error("Došlo je do greške:", error);
        });
    },
  },
  mounted() {
    this.dohvati_sve_korisnike();
  },
  computed: {
    uniqueKorisnici() {
      const seen = new Set();
      return this.korisnici.filter((k) => {
        if (seen.has(k.id)) {
          return false;
        }
        seen.add(k.id);
        return true;
      });
    },
  }
};
</script>



<style scoped>
.gradient-custom {
  /* fallback for old browsers */
  background: #fccb90;

  /* Chrome 10-25, Safari 5.1-6 */
  background: -webkit-linear-gradient(
    to right,
    #ee7724,
    #d8363a,
    #dd3675,
    #b44593
  );

  background: linear-gradient(to right, #ee7724, #d8363a, #dd3675, #b44593);
}

.card-registration .select-input.form-control[readonly]:not([disabled]) {
  font-size: 1rem;
  line-height: 2.15;
  padding-left: 0.75em;
  padding-right: 0.75em;
}
.card-registration .select-arrow {
  top: 13px;
}
</style>