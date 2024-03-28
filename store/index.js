import { createStore } from 'vuex'
import { qoutesData } from './data';

const store = createStore({
    namespaced: true,
    state: {
        quotes: qoutesData(),
        supplierQoutes: [],
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
            if (country === '') return null;
            return state.quotes.filter(
                (quote) => quote.pais === country
                )
        },
        getPortsSupplier: (state) => (supplier) => {
            if (!supplier) return '';
            return supplier.puertos.join(' - ');
        },
    },
    mutations: {
        addQuote(state, payload) {
            state.supplierQoutes.push(payload);
        },
    },
    actions: {
    },
    modules: {
    }
});
export default store;
