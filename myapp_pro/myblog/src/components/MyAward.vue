<template>
    <div>
        <p class="course">{{ date }} {{ name }}</p>
    </div>
</template>

<script>
import { onMounted } from 'vue';

export default{
    setup(){
        onMounted(() => {
            console.log(`the component is now mounted.`)
        })
    },
    props: {
        degree: { required: true, type: String },
        major: { required: true, type: String },
        date: { required: true, type: String },
        name:{ required: true, type: String },
        id:{required:true, type:String},
    },
    
}

</script>
<style scoped>

p{
    display: block;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    margin: 0;
}
p.course{
    font-size: 20px;
    font-weight: 700;
}

p.little{
    font-size: 20px;
    color: rgba(0,0,0,.6);
}


</style>