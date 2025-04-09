<template>
  <!-- Hero Section -->
  <section class="gradient-custom-2 text-white text-center py-5">
    <div class="container">
      <h1 class="display-4">Dobrodošli u naš Stomatološki Shop</h1>
      <p class="lead">Proizvodi koji čine vaš osmeh blistavim!</p>
      <a href="#proizvodi" class="btn btn-light btn-lg">Pogledajte proizvode</a>
      <router-link to="/profile"
        ><button class="btn btn-primary btn-lg m-4">
          Moj profil
        </button></router-link
      >
      <button class="btn btn-warning btn-lg m-5" @click="odjavi_se">
        Odjavi se
      </button>
    </div>
    <div>
      <button
        id="cart"
        data-bs-toggle="modal"
        data-bs-target="#korpa"
        @click="dohvati_sve_odabrane_proizvode"
      >
        Korpa
      </button>
    </div>
  </section>

  <!-- MODAL KORPA -->

  <div
    class="modal fade"
    id="korpa"
    tabindex="-1"
    aria-labelledby="korpaLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h3 class="modal-title" id="exampleModalLabel">Korpa</h3>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <p v-if="flag">
            <b
              >Korpa je trenutno prazna. Odaberite proizvode koje zelite
              kupiti.</b
            >
          </p>
          <table class="table" v-else>
            <thead>
              <tr>
                <th>Naziv proizvoda</th>
                <th>Odabrano proizvoda</th>
                <th>Cena pojedinačno</th>
                <th>Ukupna cena</th>
                <th>Prodavac</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(p, index) in odabrani_proizvodi" :key="index">
                <td>{{ p.naziv }}</td>
                <td>{{ p.kolicina_u_korpi }}</td>
                <td>{{ p.cena_proizvoda }} RSD</td>
                <td>
                  <b>{{ p.kolicina_u_korpi * p.cena_proizvoda }} RSD</b>
                </td>
                <td>
                  <i>{{ p.username }}</i>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="modal-footer">
          <button
            v-if="flag"
            type="button"
            class="btn btn-danger btn-lg"
            data-bs-dismiss="modal"
            @click="obrisi_stavke_iz_korpe"
            disabled
          >
            Obriši korpu
          </button>

          <button
            v-else
            type="button"
            class="btn btn-danger btn-lg"
            data-bs-dismiss="modal"
            @click="obrisi_stavke_iz_korpe"
          >
            Obriši korpu
          </button>

          <button
            type="button"
            class="btn btn-success btn-lg"
            data-bs-dismiss="modal"
          >
            Nastavi kupovinu
          </button>
          <button
            v-if="flag"
            type="button"
            class="btn btn-primary btn-lg"
            data-bs-dismiss="modal"
            @click="idi_na_placanje"
            disabled
          >
            Idi na plaćanje
          </button>
          <button
            v-else
            type="button"
            class="btn btn-primary btn-lg"
            data-bs-dismiss="modal"
            @click="idi_na_placanje"
          >
            Idi na plaćanje
          </button>
        </div>
      </div>
    </div>
  </div>

  
  <section id="proizvodi" class="py-5">
    <div class="container">
      <h1 class="text-center mb-5">Proizvodi u ponudi</h1>
      <div class="row">
        <div class="col-md-12">
          <div
            class="card mb-2"
            v-for="proizvod in proizvodi"
            :key="proizvod.idProizvodi"
          >
            <div class="card-body">
              <h3
                class="card-title text-center text-uppercase font-weight-bold mb-3"
              >
                {{ proizvod.naziv }}
              </h3>
              <hr />
              <p class="card-text text-muted mb-4">{{ proizvod.opis }}</p>

              <!-- Cena -->
              <h4 class="text-success mb-3">
                Cena:
                <span class="font-weight-bold">{{ proizvod.cena }} din</span>
              </h4>

              <!-- Količina na stanju -->
              <h4 class="text-primary mb-3">
                Količina na stanju:
                <span class="font-weight-bold">{{ proizvod.kolicina }}</span>
              </h4>

              <!-- Prodavac -->
              <h4 class="text-secondary mb-4">
                Prodavac:
                <span class="font-weight-bold">@{{ proizvod.username }}</span>
              </h4>

              <button
                type="button"
                class="btn btn-primary btn-lg"
                data-bs-toggle="modal"
                :data-bs-target="'#staticBackdrop' + proizvod.idProizvodi"
                v-if="!proizvod.kolicina == 0"
              >
                Kupite
              </button>
              <button
                v-else
                disabled
                type="button"
                class="btn btn-danger btn-lg"
              >
                Nema na stanju
              </button>

              <!-- Modal -->
              <div
                class="modal fade"
                :id="'staticBackdrop' + proizvod.idProizvodi"
                data-bs-backdrop="static"
                data-bs-keyboard="false"
                tabindex="-1"
                aria-labelledby="staticBackdropLabel"
                aria-hidden="true"
                v-for="proizvod in proizvodi"
                :key="proizvod.idProizvodi"
              >
                <div class="modal-dialog">
                  <div class="modal-content">
                    <div class="modal-header">
                      <h1 class="modal-title fs-5" id="staticBackdropLabel">
                        {{ proizvod.naziv }}
                      </h1>
                      <button
                        type="button"
                        class="btn-close"
                        data-bs-dismiss="modal"
                        aria-label="Close"
                      ></button>
                    </div>
                    <div class="modal-body">
                      <p>Odaberite kolicinu:</p>

                      <div
                        class="d-flex justify-content-between align-items-center m-4"
                      >
                        <div class="d-flex">
                          <button
                            class="btn btn-outline-danger btn-lg mr-2"
                            @click="oduzmi_kolicinu"
                          >
                            -
                          </button>
                          <span class="product-quantity">{{ kolicina }}</span>
                          <button
                            class="btn btn-outline-success btn-lg ml-2"
                            @click="dodaj_kolicinu(proizvod.kolicina)"
                          >
                            +
                          </button>
                        </div>
                      </div>
                      <div class="modal-footer">
                        <button
                          type="button"
                          class="btn btn-danger"
                          data-bs-dismiss="modal"
                          @click="ponisti_unetu_kolicinu"
                        >
                          Nazad
                        </button>
                        <button
                          type="button"
                          class="btn btn-primary"
                          data-bs-dismiss="modal"
                          @click="dodaj_u_korpu(proizvod)"
                        >
                          Dodaj u korpu
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="bg-dark text-white text-center py-3">
    <p>&copy; 2025 Stomatologija Shop. Sva prava zadržana.</p>
    <p>Miloš Radovanović</p>
  </footer>
</template>
  
  <script>
import axios from "axios";

export default {
  data() {
    return {
      proizvodi: [],
      kolicina: 0,
      odabrana_kolicina: 0,
      odabrani_proizvodi: [],
      ukupna_cena: 0,
      flag: false,
    };
  },
  methods: {
    async dohvati_sve_proizvode() {
      const response = await axios.get("http://127.0.0.1:5000/proizvodi");
      this.proizvodi = response.data.proizvodi;
    },

    async dohvati_sve_odabrane_proizvode() {
      try {
        const response = await axios.get(
          "http://127.0.0.1:5000/dohvati_iz_tabele_korpa_proizvodi"
        );
        console.log(response.data.message);

        this.flag = response.status === 401 ? true : false;

        if (response.status === 200) {
          this.odabrani_proizvodi = response.data.odabrani_proizvodi;
        }
      } catch (error) {
        
        console.error("Greška prilikom dohvatanja podataka: ", error);
        this.flag = true; 
        
      }
    },

    ponisti_unetu_kolicinu() {
      this.kolicina = 0;
    },
    oduzmi_kolicinu() {
      if (this.kolicina > 0) {
        this.kolicina--;
      } else {
        this.$toast.error("Kolicina ne može biti negativna!");
      }
    },
    dodaj_kolicinu(maxKolicina) {
      if (this.kolicina < maxKolicina) {
        this.kolicina++;
      } else {
        this.$toast.error("Dostigli ste maksimalan broj proizvoda na lageru!");
      }
    },
    async odjavi_se() {
      const get_korisnik = sessionStorage.getItem("korisnik");
      // const get_korpa = sessionStorage.getItem('korpa')

      const response = await axios.post("http://127.0.0.1:5000/logout", {
        korisnik: get_korisnik,
      });
      sessionStorage.clear();

      if (response.status == 200) {
        console.log(response.data.message);
        this.$router.push({ name: "login" });
        this.$toast.info("Odjavili ste se.");
      }
    },
    dodaj_u_korpu(proizvod) {
      this.flag = true;
      if (this.kolicina == 0) {
        return this.$toast.error("Prvo morate odabrati kolicinu proizvoda");
      }
      if (proizvod.kolicina >= this.kolicina) {
        proizvod.kolicina -= this.kolicina;
      }

      this.odabrana_kolicina = this.kolicina;
      console.log(this.odabrana_kolicina);
      this.kolicina = 0;

      const get_korpa = sessionStorage.getItem("korisnik");
      const get_korpa_id = JSON.parse(get_korpa);

      const data = {
        kolicina_u_korpi: this.odabrana_kolicina,
        cena: proizvod.cena,
        proizvod_id: proizvod.idProizvodi,
        korpa_id: get_korpa_id.korpa_id,
        prodavac_id: proizvod.prodavac_id,
      };

      const response = axios.post(
        "http://127.0.0.1:5000/dodaj_u_tabelu_korpa_proizvodi",
        data
      );

      return this.$toast.success("Proizvod uspesno dodat u korpu");
    },
    obrisi_stavke_iz_korpe() {
      axios.get("http://127.0.0.1:5000/obrisi_stavke_iz_korpe");
      window.location.reload();
      return this.$toast.success("Obrisali ste odabrane proizvode iz korpe!");
    },
    idi_na_placanje() {
      this.$router.push({name:'cart-view'});
    },
  },
  mounted() {
    this.dohvati_sve_proizvode();
  },
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
.card {
  transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
}

.product-quantity {
  font-size: 1.7rem;
  margin: 0 20px;
}

.card:hover {
  box-shadow: 0 4px 20px red;
}

.card-body {
  padding: 20px;
}

.card-title {
  font-size: 1.5rem;
  color: #333;
}

.card-text {
  font-size: 1rem;
  color: #666;
}

h4 {
  font-size: 1.2rem;
  color: #28a745;
}

h5 {
  font-size: 1rem;
  color: #6c757d;
}

.text-success {
  color: #28a745 !important;
}

.text-secondary {
  color: #6c757d !important;
}

.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
}

.btn-primary:hover {
  background-color: #0056b3;
  border-color: #0056b3;
}

.btn-outline-secondary {
  border-color: #6c757d;
  color: #6c757d;
}

.btn-outline-secondary:hover {
  background-color: #6c757d;
  color: #fff;
}
#cart {
  --width: 150px;
  --timing: 2s;
  border: 0;
  width: var(--width);
  padding-block: 1em;
  color: #fff;
  font-weight: bold;
  font-size: 1.5em;
  background: rgb(64, 192, 87);
  transition: all 0.2s;
  border-radius: 8px;
  cursor: pointer;
}
#cart:hover {
  background-image: linear-gradient(
    to right,
    #ee7724,
    #d8363a,
    #dd3675,
    #b44593
  );
  animation: var(--timing) linear dance6123 infinite;
  transform: scale(1.1) translateY(-1px);
}
@keyframes dance6123 {
  to {
    background-position: var(--width);
  }
}
.modal-footer {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.modal-footer .btn {
  margin: 0 5px; 
}

.modal-footer .btn-danger {
  margin-right: auto; 
}
</style>
