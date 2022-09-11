<template>
  <el-carousel :interval="4000" type="card" height="380px" class = "cardsClass">
    <el-carousel-item  class = "customerCardItem" key = 1 shadow="always">
      <el-card class="customerCardClass">
        <el-row class = "customerCardRow">
          <el-col :span="12" class = "customerForm1Col">
              <customer-form-1/>
          </el-col>

          <el-col :span="12" class = "customerForm2Col">
              <customer-form-2/>
          </el-col>
        </el-row>
      </el-card>
    </el-carousel-item>

     
    <el-carousel-item class = "managerCardItem" key = 2 shadow="always">
      <el-card class="managerCardClass">
        <el-row class = "managerCardRow">
          <el-col :span="12" class = "managerForm1Col">
              <manager-form-1/>
          </el-col>

          <el-col :span="12" class = "managerForm2Col">
              <manager-form-2/>
          </el-col>
          
        </el-row>
      </el-card>
    </el-carousel-item>


    <el-carousel-item class = "businessCardItem" key = 3 shadow="always">
      <el-card class="businessCardClass">
        <el-row class = "businessCardRow">
          <el-col :span="12" class = "businessForm1Col">
              <business-form-1/>
          </el-col>

          <el-col :span="12" class = "businessForm2Col">
              <business-form-2/>
          </el-col>
          
        </el-row>
      </el-card>
    </el-carousel-item>


  </el-carousel>
</template>

<script>
import customerForm1 from './customerForm1.vue'
import customerForm2 from './customerForm2.vue'
import customerCard from './customerCard.vue'
import businessForm1 from './businessForm1.vue'
import businessForm2 from './businessForm2.vue'
import managerForm1 from './managerForm1.vue'
import managerForm2 from './managerForm2.vue'

export default {
  name: 'cards',
  components: {
    customerForm1,
    customerForm2,
    businessForm1,
    businessForm2,
    managerForm1,
    managerForm2,
    customerCard,
  }
}
</script>

<style>

.cardsClass {
  background-color: #f8d76c;
  border-radius: 20px;
}

.el-carousel__item:nth-child(2n){
  background-color:   #fdf9e7;
  border-radius: 20px;
  width: 660px;
  height: 330px;
  margin-left: 90px;
  margin-top:30px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.07), 
                0 2px 4px rgba(0,0,0,0.07), 
                0 4px 8px rgba(0,0,0,0.07), 
                0 8px 16px rgba(0,0,0,0.07),
                0 16px 32px rgba(0,0,0,0.07), 
                0 32px 64px rgba(0,0,0,0.07);
  
}

.el-carousel__item:nth-child(2n + 1) {
  /* background-color: white; */
  background-color:   #fdf9e7;
  border-radius: 20px;
  width: 660px;
  height: 330px;
  margin-left: 90px;
  margin-top:30px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.07), 
                0 2px 4px rgba(0,0,0,0.07), 
                0 4px 8px rgba(0,0,0,0.07), 
                0 8px 16px rgba(0,0,0,0.07),
                0 16px 32px rgba(0,0,0,0.07), 
                0 32px 64px rgba(0,0,0,0.07);
  
}

</style>
