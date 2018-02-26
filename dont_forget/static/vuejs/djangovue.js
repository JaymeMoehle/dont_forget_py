

const noteapp = new Vue({
  el: '#noteapp',
  delimiters: ['${','}'],
  data: {
    title: "Don't Forget",
    note: [],

  },

  http: {
      root: 'http://localhost:8000/api',

       },


  methods: {

    addNote: function() {
      this.$http.post('note/',this.addNote)
          .then((response) => {
          })
          .catch((err) => {
            console.log(err);
          })
    },
    updateNote: function() {
      this.$http.put(`note/${this.currentNote.note_id}/`, this.currentNote)
          .then((response) => {
            this.currentNote= response.data;

          })
          .catch((err) => {
            console.log(err);
          })
    },
    deleteNote: function(id) {
      this.$http.delete(`note/${id}/`)
          .then((response) => {


          })
          .catch((err) => {
            console.log(err);
          })
    }
  },

  mounted: function(){
     this.$http.get('note/').then(function(response){
       this.note = response.data

     }),
       function(response){
         console.log(response)
       }

   },
});
