<template>
    <form @submit.prevent="onSubmit">
        <label for="new-todo-input"> What needs to be done? </label>
            <input type="text"  id="new-todo-input" name="new-todo" autocomplete="off"  v-model.lazy.trim="label"
            class="input__lg"
            />
        <button type="submit" class="btn btn__primary btn__lg">Add</button>
    </form>
</template>

<script>
    export default {
        methods: {
            onSubmit() {
                console.log('Label value: ', this.label);
                if(this.label == "" || this.label === undefined) {
                    return;
                }
                this.$emit('todo-added', this.label)
                this.label = "";
            },
        },
    }
</script>