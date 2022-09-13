<template>
    <el-form 
      :model="form"
      :rules="rules"
      ref="form"
      class="storeForm2"
    >
        <el-form-item class = "titleClass">
            <h3 class = "title">
                我是商家
            </h3>
        </el-form-item>
    </el-form>

</template>

<script lang="ts" setup>

</script>

<style>
.storeForm2 {
    height: 300px;
    width: 300px;
    margin-top: 0px;
    margin-bottom: 0px;
    margin-left: 0px;
    margin-right: 0px;
    background-color: white;
}

.titleClass {
    float: right;
    margin-top: 70px;
    margin-bottom: auto;
    margin-right:30px;
}
.title {
    width: 30px;
    font-size: 30px;
    font-weight: bold;
    color: black;
    margin-top: 0px;  
}

</style>