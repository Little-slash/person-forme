<template>
    <div>
        &lt;{{name}}&gt; 
        <p class="course">{{ date }} {{ title }},{{ DOI }}</p>
        <p class="little" ><a :href="url">INDEX</a></p>
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
        DOI: { required: true, type: String },    // DOI or github
        title: { required: true, type: String },       // 项目或文章名称
        date: { required: true, type: String },   //日期
        name:{ required: true, type: String },    //第几作者 （1）（2）
        id:{required:true, type:String},
        url:{required:true,type:URL},      //项目或文章地址
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