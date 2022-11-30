<template>
    <n-card class = "shoppingCartClass" embedded>
      <el-row>
        <el-col :span="8">
          <img :src="{logo}" class = "shoppingCartImageClass">
        </el-col>
        <el-col :span="16">
          <h3 class = "shoppingCartName">{{name}}</h3>
          <el-row>
            <el-col :span="12"><h3 class = "shoppingCartPrice">￥{{price}}</h3></el-col>
            <el-col :span="12">
              <el-input-number v-model="num" :min="1" :max="100" @change="handleChange"  class = "numInputClass"/>
            </el-col>
          </el-row>
        </el-col>
      </el-row>
  </n-card>
</template>
  
  <script>
  import { defineComponent } from "vue";
  import {NCard} from "naive-ui";

  export default defineComponent({
    components: {
      NCard,
    },
    props:{
      logo:{
        type:String
      },
      name:{
        type:String
      },
      price:{
        type:Number
      }
    }
  });
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