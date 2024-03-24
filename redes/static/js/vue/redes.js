new Vue({
    delimiters: ['[[', ']]'],
    el:'#appRedes',
    data:{
        lists: [],
        form:{ fields:{} },
        errors: [],
    },
    created:function(){
        this.listRedes();
    },
    methods:{
        listRedes:function(){
            axios({
                method: 'GET',
                url: 'api/',
                responseType: 'json'
            })
            .then(response =>{
                this.lists = response.data
            })
            .catch(e => {
                this.errors.push(e)
            })
        },

        editRed: function(_param, key){
            this.findkey = key;
            this.form = _param;
        },

        updateRed:function(e){
            var csrfmiddlewaretoken =  document.getElementsByName('csrfmiddlewaretoken')[0].value
            var bodyFormData = new FormData(e.target);
            bodyFormData.set('eid', this.form.fields.eid[0]);
            axios({
                headers: {'X-CSRFToken': csrfmiddlewaretoken},
                method: 'PUT',
                url: 'api/',
                data: bodyFormData,
            }).then(response =>{
                this.listRedes();
                new PNotify({
                    title: 'Actualizado!',
                    text: 'Datos actualizados correctamente...',
                    type: 'success',
                    styling: 'fontawesome',
                    delay: 3000,
                });

                $("#modalRed").modal('hide');
            }).catch(e => {
                this.errors.push(e)
            })
        },
    },
})