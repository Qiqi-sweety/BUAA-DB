<!--TODO: 接口没好-->
<template>
    <n-card class = "shoppingCartClass" embedded>
      <el-row>
        <el-col :span="8">
          <img :src="`/api${item.logo}`" class = "shoppingCartImageClass">
        </el-col>
        <el-col :span="16">
          <h3 class = "shoppingCartName">{{item.name}}</h3>
          <el-row>
            <el-col :span="12"><h3 class = "shoppingCartPrice">￥{{price}}</h3></el-col>
            <el-col :span="12">
              <el-input-number v-model="item.num" :min="1" :max="100" @change="handleChange"  class = "numInputClass"/>
            </el-col>
          </el-row>
        </el-col>
      </el-row>
  </n-card>
</template>
  
  <script setup>
  import {NCard} from "naive-ui";


  </script>
  
  <style>
  .shoppingCartClass {
    width: 450px;
    height: 150px;
  }

  .shoppingCartImageClass {
    width: 110px;
    height: 110px;
  }

  .shoppingCartName {
    font-size:17px;
  }

  .shoppingCartPrice {
    color: red;
    margin-top: 10px;
  }

  .numInputClass {
    margin-top: 10px;
  }
  
  </style>