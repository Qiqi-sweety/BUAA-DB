<!-- userOrderPage的子组件：页面的顶部导航栏 -->

<template>
  <el-row
  style = "background-color: white;
    width: 95%;
    margin-bottom: 20px;
    margin-left: auto;
    margin-right: auto;">
    <el-col :span="12">
      
      <el-menu
        default-active="0"
        class="el-menu-demo"
        mode="horizontal"
        :ellipsis="false"
        @select="handleSelect"
      >
        <el-menu-item index="0">首页</el-menu-item>
        <el-menu-item index="1">商品</el-menu-item>
        <el-menu-item index="2">评价</el-menu-item>
      </el-menu>
    </el-col>
    <el-col :span="8">
      <el-input
        v-model="input"
        placeholder="搜索商品"
        class="input-with-select"
      >
      <template #append>
        <el-button @click="act_search">
          <el-icon>
                <Search/>
          </el-icon>
        </el-button>
      </template>
    </el-input>
    
    </el-col>
    <el-col :span="4">
      
      <n-button @click="activate" type="warning" size="large" class = "shoppingButtonClass">
          查看购物车
      </n-button>
    
    </el-col>
  </el-row>

  <n-drawer v-model:show="active" width="502">
    <n-drawer-content closable>
      <template #header>
        购物车
      </template>
      <div v-for="item in cart.items">
        <shoppingCart :item="item"/>
      </div>
      <template #footer >
        <h3 style = "font-size: 18px;
                    /* color: red; */
                    margin-left: 0;
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
  <script setup>
  import {reactive, ref} from 'vue'
  import {NButton, NDrawer, NDrawerContent, NPopconfirm} from 'naive-ui'
  import {ElMessage} from 'element-plus'
  import {make_order, show_cart} from "@/api/userMain";
  import {useRouter} from "vue-router";
  const router = useRouter()

  let input = ref('')
  const cart = reactive({
    items: []
  })

  const props = defineProps({store_id: String})

  const active = ref(false)
  const activate = () => {
    active.value = true
    show_cart({
      store_id: props.store_id
    }).then(res => {
      let content = res.data
      console.log(content)
      if (content.code === "200") {
        content.items.forEach(item => {
          cart.items.push(item)
        })
      }
    })
  }

  const handlePositiveClick = () => {
    make_order({
      store_id: props.store_id
    }).then(res => {
      let content = res.data
      console.log(content)
      if (content.code === "200") {
        ElMessage({message: "下单成功，商家正在准备订单！", type: "success"})
      } else {
        ElMessage({message: content.message, type: "error"})
      }
    })
  }
  const handleNegativeClick = () => {
  }

  const handleSelect = (key) => {
    if (key === "0") {
      router.push({
        name: 'homePageCard',
        query: {store_id: props.store_id}
      })
    } else if (key === "1") {
      router.push({
        name: 'menuPageCard',
        query: {store_id: props.store_id}
      })
    } else if (key === "2") {
      router.push({
        name: 'evaluatePageCard',
        query: {store_id: props.store_id}
      })
    }
  }
  const act_search = () => {
    router.push({
      name: 'resultPageCard',
      query: {store_id: props.store_id, msg: input.value}
    })
  }
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
  