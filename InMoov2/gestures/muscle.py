
def muscle():
  inMoov.startedGesture()
  inMoov.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
  inMoov.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  inMoov.setArmVelocity("right", 31.0, 43.0, 59, 43.0)
  inMoov.setArmVelocity("left", 31.0, 43.0, 59, 43.0)
  inMoov.setHeadVelocity(22.0, 22.0)
  inMoov.setTorsoVelocity(31.0, 13.0, -1)
  inMoov.moveHead(90,129)
  inMoov.moveArm("left",90,139,48,75)
  inMoov.moveArm("right",71,40,14,43)
  inMoov.moveHand("left",180,180,180,180,180,148)
  inMoov.moveHand("right",99,130,152,154,145,180)
  inMoov.moveTorso(120,100,90)
  sleep(4)
  inMoov.mouth.speakBlocking("Looks good, doesn't it")
  #inMoov.mouth.speakBlocking(u"Выглядит хорошо, не так ли?")
  sleep(2)
  inMoov.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
  inMoov.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  inMoov.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
  inMoov.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  inMoov.setHeadVelocity(43.0, 43.0)
  inMoov.setTorsoVelocity(31.0, 13.0, -1)
  inMoov.moveHead(90,45)
  inMoov.moveArm("left",44,46,20,39)
  inMoov.moveArm("right",90,145,58,74)
  inMoov.moveHand("left",180,180,180,180,180,83)
  inMoov.moveHand("right",99,130,152,154,145,21)
  inMoov.moveTorso(60,75,90)
  sleep(3)
  inMoov.mouth.speakBlocking("not bad either, don't you think")
  #inMoov.mouth.speakBlocking(u"Неплохо, не так ли?")
  sleep(4)
  inMoov.finishedGesture()
  relax()
  sleep(1)
