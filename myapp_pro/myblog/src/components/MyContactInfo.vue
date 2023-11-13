<template>
      <div class="rightblock">
        <b :id="id">{{ label }}</b>{{ info }}
      </div>
  </template>
  <script>
  import uniqueId from "lodash.uniqueid";

  export default {
    components: {
    },
      props: {
          label: { required: true, type: String },
          info: { required: false, type: String },
          id: {required:true, type:String},
    },
      data() {
          return {
            id: uniqueId("to-do-"),
        }
    },
    computed: {
    },
    methods: {
      
    }
  };
</script>

<style scoped>
/**fgf */
  html{
    font-family: 'JetBrainsMono-Regular';
  }
  b, strong {
    font-weight: bold;
  }
</style>