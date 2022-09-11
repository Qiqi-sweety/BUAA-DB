<template>
    <el-form 
      :model="form"
      :rules="rules"
      ref="form"
      class="customerForm1"
    >
        <el-form-item class = "logoFormItem">

            <img alt="loginLogo" src="../../assets/customerLogo.svg" class = "logo" >

      
        </el-form-item>

        <el-form-item class = "detailFormItem">
            <p class = "details">
            吃饱了才有力气减肥！
            </p>
        </el-form-item>




    </el-form>
  

</template>

<script lang="ts" setup>

</script>

<style>

.customerForm1 {
    /* border:5px solid red; */
    width: 250px;
    height: 300px;
    background-color: white;
    margin-top: 0px;
    margin-bottom: 0px;
    margin-left: 0px;
    margin-right: 0px;

}

.logoFormItem {
    margin-bottom: 0px;
}

.logo {
    width: 250px;
    height: 250px;
}

.detailFormItem {
    margin-left: 40px;
    margin-bottom: 0px;
}

.details {
    margin-top: 0px;
    padding: 0px;
    color :#606266;
    font-family: "微软雅黑";
    font-weight:bold;
    font-size: 18px;
}




</style>