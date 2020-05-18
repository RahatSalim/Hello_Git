Spend by category conversion code

import React, {useState, useEffect} from 'react';
import {connect} from 'react-redux';
import {View, Text, Image, TouchableOpacity, StyleSheet} from 'react-native';
import colors from '../config/color';
import moment from 'moment';

const SpendByCategory = ({azureData, loading, error}) => {
const [selectedButton, setSelectedButton] = useState(2);
const [serverlessValue, setValueServerless] = useState([]);
const [databaseValue, setDatabaseValue] = useState([]);
const [computeValue, setComputeValue] = useState([]);

const SelectionOnPressForSixMonth = data => {
let dataSeries = [];

    let startDate = moment(new Date()).format('YYYY-MM-DD');
    var makeDate = new Date();
    makeDate.setMonth(makeDate.getMonth() - Number(data));
    let endDate = moment(makeDate, 'YYYY-MM-DD').format('YYYY-MM-DD');

    const dataYearly = azureData.data.yearly;

    for (let yearlyObj of dataYearly) {
      let year = yearlyObj.year;
      for (let subscriptionsWiseObj of yearlyObj.tenants.subscriptions) {
        subscriptionsWiseObj.monthWiseSpendByCategory.filter((item: any) => {
          let month = year + '-' + item.month;
          let fromDate = startDate;
          let toDate = endDate;

          if (month >= toDate && month <= fromDate) {
            dataSeries.push({
              month: month,
              serverless: item.serverless,
              compute: item.compute,
              database: item.database,
              storage: item.storage,
              containers: item.containers,
              other: item.other,
            });
          }
          return month >= toDate && month <= fromDate;
        });
      }
    }

    let serverlessCost = 0;
    let databaseCost = 0;
    let computeCost = 0;

    for (let month of dataSeries) {
      if (month.serverless) {
        if (month.serverless.compute.length > 0) {
          for (let compute of month.serverless.compute) {
            let temp = Number(serverlessCost) + Number(compute.cost);
            serverlessCost = Number(temp).toFixed(2);
          }
        }
        if (month.serverless.database.length > 0) {
          for (let database of month.serverless.database) {
            let temp = Number(serverlessCost) + Number(database.cost);
            serverlessCost = Number(temp).toFixed(2);
          }
        }
        if (month.serverless.networkingAndCdn.length > 0) {
          for (let networkcdn of month.serverless.networkingAndCdn) {
            let temp = Number(serverlessCost) + Number(networkcdn.cost);
            serverlessCost = Number(temp).toFixed(2);
          }
        }
        if (month.serverless.application_integration) {
          for (let application_integration of month.serverless
            .application_integration) {
            let temp =
              Number(serverlessCost) + Number(application_integration.cost);
            serverlessCost = Number(temp).toFixed(2);
          }
        }
        if (month.serverless.analytics) {
          for (let analytics of month.serverless.analytics) {
            let temp = Number(serverlessCost) + Number(analytics.cost);
            serverlessCost = Number(temp).toFixed(2);
          }
        }
        setValueServerless(serverlessCost);
      }
      // if (month.storage) {
      //   if (month.storage.storageAccounts.length > 0) {
      //     for (let storage of month.storage.storageAccounts) {
      //       let temp = Number(storageCost) + Number(storage.cost);
      //       storageCost = Number(temp).toFixed(2);
      //     }
      //   }
      // }
      if (month.database) {
        if (month.database.database.length > 0) {
          for (let database of month.database.database) {
            let temp = Number(databaseCost) + Number(database.cost);
            databaseCost = Number(temp).toFixed(2);
          }
        }
        setDatabaseValue(databaseCost);
      }
      if (month.compute) {
        if (month.compute.compute.length > 0) {
          for (let compute of month.compute.compute) {
            let temp = Number(computeCost) + Number(compute.cost);
            computeCost = Number(temp).toFixed(2);
          }
        }
        setComputeValue(computeCost);
      }
      // if (month.other) {
      //   if (month.other.other.length > 0) {
      //     for (let other of month.other.other) {
      //       let temp = Number(othersCost) + Number(other.cost);
      //       othersCost = Number(temp).toFixed(2);
      //     }
      //   }
      // }
      // if (month.containers) {
      //   if (month.containers.containers.length > 0) {
      //     for (let container of month.containers.containers) {
      //       let temp = Number(containerCost) + Number(container.cost);
      //       containerCost = Number(temp).toFixed(2);
      //     }
      //   }
      // }
    }

};

useEffect(() => {
SelectionOnPressForSixMonth(6);
}, []);

return (
<View
style={{
        backgroundColor: colors.lightblack,
        borderRadius: 12,
        borderWidth: 0.1,
        marginLeft: 8,
        marginRight: 8,
        marginBottom: 8,
      }}>
<Text
style={{
          fontSize: 24,
          fontWeight: 'bold',
          color: colors.white,
          marginLeft: 8,
        }}>
Spend by Category
</Text>

      <View
        style={{
          flexDirection: 'row',
          padding: 7,
          justifyContent: 'space-between',
        }}>
        <View
          style={{
            backgroundColor: '#31BEF3',
            width: 115,
            height: 175,
            borderRadius: 15,
            shadowRadius: 6,
            shadowOpacity: 0.26,
            elevation: 5,
            shadowColor: 'blue',
            shadowOffset: {width: 0, height: 2},
          }}>
          <View
            style={{
              flexDirection: 'column',
              padding: 8,
            }}>
            <Text
              style={{
                fontSize: 15,
                // fontFamily: 'OpenSans-Light',
                color: colors.white,
                fontWeight: 'bold',
                // alignSelf: 'flex-start',
                alignSelf: 'center',
              }}>
              Compute
            </Text>

            <Text
              style={{
                fontSize: 20,
                fontFamily: 'OpenSans-Light',
                color: colors.darkblack,
                marginLeft: 18,
                marginVertical: 33,
                fontWeight: 'bold',
              }}>
              ${computeValue}
            </Text>

            <Image
              source={require('../image/cloud-icon.png')}
              style={{
                marginLeft: 18,
                height: 40,
                width: 40,
              }}
            />
          </View>
        </View>

        <View
          style={{
            backgroundColor: '#08619D',
            width: 115,
            height: 175,
            borderRadius: 15,
            shadowRadius: 6,
            shadowOpacity: 0.26,
            elevation: 5,
            shadowColor: 'blue',
            shadowOffset: {width: 0, height: 2},
          }}>
          <View
            style={{
              flexDirection: 'column',
              padding: 8,
            }}>
            <Text
              style={{
                fontSize: 15,
                fontFamily: 'OpenSans-Light',
                color: colors.white,
                fontWeight: 'bold',
                textAlign: 'center',
              }}>
              Database
            </Text>

            <Text
              style={{
                fontSize: 20,
                fontFamily: 'OpenSans-Light',
                color: colors.darkblack,
                marginLeft: 18,
                marginVertical: 31,
                fontWeight: 'bold',
              }}>
              ${databaseValue}
            </Text>

            <Image
              source={require('../image/database-icon.png')}
              style={{
                marginLeft: 18,
                height: 40,
                width: 40,
              }}
            />
          </View>
        </View>

        <View
          style={{
            backgroundColor: '#FBD63D',
            width: 115,
            height: 175,
            borderRadius: 15,
            shadowRadius: 6,
            shadowOpacity: 0.26,
            elevation: 5,
            shadowColor: 'blue',
            shadowOffset: {width: 0, height: 2},
          }}>
          <View
            style={{
              flexDirection: 'column',
              padding: 8,
            }}>
            <Text
              style={{
                fontSize: 15,
                fontFamily: 'OpenSans-Light',
                color: colors.white,
                fontWeight: 'bold',
                textAlign: 'center',
              }}>
              Serverless
            </Text>

            <Text
              style={{
                fontSize: 20,
                fontFamily: 'OpenSans-Light',
                color: colors.darkblack,
                marginLeft: 18,
                marginVertical: 31,
                fontWeight: 'bold',
              }}>
              ${serverlessValue}
            </Text>

            <Image
              source={require('../image/severless-icon.png')}
              style={{
                marginLeft: 18,
                height: 40,
                width: 40,
              }}
            />
          </View>
        </View>
      </View>

      <View
        style={{
          flexDirection: 'row',
          justifyContent: 'space-evenly',
          padding: 8,
        }}>
        <TouchableOpacity
          onPress={() => {
            SelectionOnPressForSixMonth(1);
            setSelectedButton('0');
          }}
          style={selectedButton == 0 ? styles.btnActive : styles.btnNonActive}>
          <Text style={{color: colors.white, fontSize: 18}}>1M</Text>
        </TouchableOpacity>
        <TouchableOpacity
          onPress={() => {
            SelectionOnPressForSixMonth(3);
            setSelectedButton('1');
          }}
          style={selectedButton == 1 ? styles.btnActive : styles.btnNonActive}>
          <Text
            style={{
              color: colors.white,
              fontSize: 18,
            }}>
            3M
          </Text>
        </TouchableOpacity>
        <TouchableOpacity
          onPress={() => {
            SelectionOnPressForSixMonth(6);
            setSelectedButton('2');
          }}
          style={selectedButton == 2 ? styles.btnActive : styles.btnNonActive}>
          <Text style={{color: colors.white, fontSize: 18}}>6M</Text>
        </TouchableOpacity>
        <TouchableOpacity
          onPress={() => {
            SelectionOnPressForSixMonth(12);
            setSelectedButton('3');
          }}
          style={selectedButton == 3 ? styles.btnActive : styles.btnNonActive}>
          <Text style={{color: colors.white, fontSize: 18}}>1Y</Text>
        </TouchableOpacity>
      </View>
    </View>

);
};

const styles = StyleSheet.create({
btnActive: {
backgroundColor: colors.skyblue,
width: 30,
height: 30,
borderRadius: 7,
shadowRadius: 5,
alignItems: 'center',
justifyContent: 'center',
},
btnNonActive: {
backgroundColor: colors.lightblack,
},
});

const mapStateToProps = state => {
return {
azureData: state.azureSpentReducer.azureData,
loading: state.azureSpentReducer.loading,
error: state.azureSpentReducer.error,
};
};
const mapDispatchToProps = d => {
return {
d: d,
};
};

export default connect(
mapStateToProps,
mapDispatchToProps,
)(SpendByCategory);
