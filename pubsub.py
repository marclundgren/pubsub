from pymitter import EventEmitter
import time

ee = EventEmitter()

# global state
hasCash = False # note: this is the valid amount of cash needed to advance to the next stage
def resetState(): 
    global hasCash
    hasCash = False

@ee.on("valid-cash-amount-received")
def acceptsCash():
    global hasCash
    hasCash = True
# @todo
# @ee.emit("valid-cash-amount-received")

@ee.on("invalid-cash-amount-received")
def rejectsCash():
    global hasCash
    hasCash = False
# @todo
# @ee.emit("invalid-cash-amount-received")

@ee.on("valid-knock-detected")
def validKnockDetected():
    print("Valid knock detected")
    global hasCash
    if (hasCash):
        ee.emit("knock-success")
    else:
        ee.emit("knock-partial-success")
        

@ee.on("invalid-knock-detected")
def invalidKnockDetected():
    print("Invalid knock detected")
    ee.emit("knock-failure")

@ee.on("knock-success")
def onKnockSuccess():
    print("knock success")

@ee.on("knock-failure")
def onKnockFailure():
    print("knock failure")

@ee.on("knock-partial-success")
def onKnockPartialSuccess():
    print("knock partial success")
    # @todo do something!

# def main():
  # connects the knocker
  # connect the cash grab!

def testMain():
  resetState() # Arrange
  # 1
  # Act
  ee.emit("invalid-knock-detected") 
  time.sleep(2)
  ee.emit("valid-knock-detected")
  time.sleep(5)
  ee.emit("invalid-cash-amount-received")
  time.sleep(7)
  ee.emit("valid-knock-detected")
  time.sleep(1)
  ee.emit("valid-cash-amount-received")
  time.sleep(4)
  ee.emit("valid-knock-detected")
  
  # Assert
  # Invalid knock detected
  # knock failure
  # Valid knock detected
  # knock partial success
  # Valid knock detected
  # knock partial success
  # Valid knock detected
  # knock success

def testQuick():
  resetState()
  # 1
  ee.emit("invalid-knock-detected") 
  # assert: .... print

  # 2 
  ee.emit("valid-knock-detected")


  # 3
  ee.emit("valid-cash-amount-received")

  # 4
  ee.emit("valid-knock-detected")
  # assert: success!

testMain()
# testQuick()

