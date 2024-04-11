const baseUrl = 'http://localhost:8000/'
const idUser = 0
const idForwarder = 0

const serverConfig = {
  getForwarder: `${baseUrl}api/forwarder/${idForwarder}/`,
  createForwarder: `${baseUrl}api/forwarder/create/`,
  updateForwarder: `${baseUrl}api/forwarder/update/`,
  getQoute: `${baseUrl}api/qoutation/{idQoute}/`,
  createQoute: `${baseUrl}api/qoutation/create/`,
  updateQoute: `${baseUrl}api/qoutation/update/`,
  deleteQoute: `${baseUrl}api/qoutation/delete/`,
  getUser: `${baseUrl}api/user/${idUser}/`,
  createUser: `${baseUrl}api/user/create/`,
  updateUser: `${baseUrl}api/user/update/`
}

export default serverConfig
