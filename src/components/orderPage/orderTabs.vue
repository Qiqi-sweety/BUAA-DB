<!-- userOrderPage的子组件：页面的顶部导航栏 -->

<!-- TODO：
首页按钮传递信号给userOrderPage，userOrderPage展示子组件homePageCard
商品按钮传递信号给userOrderPage，userOrderPage展示子组件manuPageCard
评价按钮传递信号给userOrderPage，userOrderPage展示子组件evaluatePageCard
进行搜索操作，将信号传递给userOrderPage，userOrderPage展示子组件resultPageCard
查看购物车按钮，可以查看购物车内容，点击购物车内的结算按钮将购物车信息与后端交互 -->

<template>
  <el-row
  style = "background-color: white;
    width: 95%;
    margin-bottom: 20px;
    margin-left: auto;
    margin-right: auto;">
    <el-col :span="12">
      
      <el-menu
    :default-active="activeIndex"
    class="el-menu-demo"
    mode="horizontal"
    :ellipsis="false"
    @select="handleSelect"
  >
    <el-menu-item index="0">首页</el-menu-item>
    <el-menu-item index="1">商品</el-menu-item>
    <el-menu-item index="3">评价</el-menu-item>
  </el-menu>
    </el-col>
    <el-col :span="8">
      <el-input
        v-model="input3"
        placeholder="搜索商品"
        class="input-with-select"
        >
      <template #append>
        <el-button>
          <el-icon>
                <Search/>
            </el-icon>
        </el-button>
      </template>
    </el-input>
    
    </el-col>
    <el-col :span="4">
      
      <n-button @click="activate" type="warning" size="large" class = "shoppingButtonClass"  > 
          查看购物车
      </n-button>
    
    </el-col>
  </el-row>

  <n-drawer v-model:show="active" :width="502">
    <n-drawer-content closable>
      <template #header>
        购物车
      </template>
      
      <shoppingCart/>
      <shoppingCart/>
      <shoppingCart/>

      <template #footer >
        <h3
        style = "    font-size: 18px;
                /* color: red; */
                margin-left:0%;
                margin-top: 5px;
                width: 250px;"
        >合计：</h3>
        <n-popconfirm
          @positive-click="handlePositiveClick"
          @negative-click="handleNegativeClick"
        >
          <template #trigger>
            <n-button type="warning" size = "large" class = "payClass">结算</n-button>
          </template>
          确认下单？
        </n-popconfirm>
      </template>
    </n-drawer-content>
  </n-drawer>

</template>
  <script>
  import { defineComponent ,ref } from 'vue'
  import { NCard , NTabs, NTabPane ,NButton ,NDrawer,NDrawerContent,NPopconfirm,useMessage} from 'naive-ui'
  import foodCard2 from "../cards/foodCard2.vue"

  import shoppingCart from "../cards/shoppingCart.vue"

  export default defineComponent({
    components: {
      NCard,
      NTabs,
      NTabPane,
      NButton,
      NDrawer,
      NDrawerContent,
      NPopconfirm,
      foodCard2,
      shoppingCart,
    },
    setup () {
    const active = ref(false)
    const activate = () => {
      active.value = true
    }
    
    const message = useMessage();
    return {
      active,
      activate,
      handlePositiveClick() {
        message.success("商家开始准备订单")
      }
    }

  }
  })
  </script>
  <style>

  .shoppingButtonClass {
    margin-top:20px;
    margin-left:50px ;
    width: 150px;
  }

  .storeTitleClass {
    font-size: 30px;
    margin-left:5%
  }

  .foodTabClass {
    margin-top:5%;
  }

  .input-with-select {
    margin-top: 25px;
  
  }

  .payClass {
    margin-right: 50px;
    width: 100px;
  }
  
  .emptyClass {
    width: 100px;
  }

  .el-menu-demo {
    height:80px;
  }

  </style>
  