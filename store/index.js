import { createStore } from 'vuex'
import { qoutesData } from './data'

const store = createStore({
  namespaced: true,
  state: {
    quotes: qoutesData(),
    supplierQoutes: []
  },
  getters: {
    getCountries: (state) => {
      return state.quotes
        .filter((quote, idx, o_array) => {
          if (o_array.findIndex((q) => q.pais === quote.pais) === idx) {
            return true
          }
        })
        .map((q) => q.pais)
        .sort()
    },
    getSupplier: (state) => (country) => {
      if (country === '') return null
      return state.quotes.filter((quote) => quote.pais === country)
    },
    getPortsSupplier: (state) => (supplier) => {
      if (!supplier) return ''
      return supplier.puertos.join(' - ')
    },
    getQoutes: (state, rootStare) => {
      if (state.supplierQoutes.length > 0) {
        return state.supplierQoutes
      }
      if (localStorage.getItem('supplierQoutes')) {
        state.supplierQoutes = JSON.parse(localStorage.getItem('supplierQoutes'))
      }
      return []
    },
    getQoute: (state) => (supplier) => {
      if (state.supplierQoutes.length === 0) return false
      const quote = state.supplierQoutes.find((quote) => quote.supplier.nombre === supplier.nombre)
      return {
        qoute: quote,
        idx: state.supplierQoutes.indexOf(quote)
      }
    },
    getSuppliersQouted: (state) => (nameSupplier) => {
      if (state.supplierQoutes.length === 0) return false

      const filtered = state.supplierQoutes.filter((i) => {
        return i.supplier.nombre === nameSupplier
      })
      if (filtered.length) return true
      return false
    }
  },
  mutations: {
    addQuote(state, payload) {
      state.supplierQoutes.push(payload)
      localStorage.clear()
      localStorage.setItem('supplierQoutes', JSON.stringify(state.supplierQoutes))
    },
    deleteQoute(state, payload) {
      state.supplierQoutes = state.supplierQoutes.filter((quote) => quote !== payload)
      localStorage.clear()
      localStorage.setItem('supplierQoutes', JSON.stringify(state.supplierQoutes))
    },
    loadSupplierQoutes: (state) => (qoutes) => {
      state.supplierQoutes = qoutes
    },
    changeQoute(state, payload) {
      localStorage.clear()
      localStorage.setItem('supplierQoutes', JSON.stringify(state.supplierQoutes))
    }
  },
  actions: {
    sendData({ commit }, payload) {
      const url = 'localhost:8000/'
    }
  }
})
export default store
