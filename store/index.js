import { createStore } from 'vuex'
import { qoutesData } from './data';

const store = createStore({
    namespaced: true,
    state: {
        quotes: qoutesData(),
    },
    getters: {
        getCountries: (state) => {
            return state.quotes.filter((quote, idx, o_array) => {
                if (o_array.findIndex((q) => q.pais === quote.pais) === idx) {
                    return true
                }
            }).map((q)=>q.pais).sort();
        },
        getSupplier: (state) => (country) => {
            return state.quotes.filter(
                (quote) => quote.pais === country
                ).map(q=>q.nombre).sort();
        },
    },
    mutations: {
    },
    actions: {
    },
    modules: {
    }
});
export default store;