<template>
  <el-input
    v-model="input"
    type="password"
    placeholder="密码"
    show-password
    size = "large"
    class = "passwordInputBox"
    
    
  >
    <template #prefix>
          <el-icon class="el-input__icon"><lock /></el-icon>
    </template>

  </el-input>
  
</template>

<script lang="ts" setup>


</script>

<style>
  .passwordInputBox {
    /* size */
    
    width: 300px;
    
    
  }

</style>





