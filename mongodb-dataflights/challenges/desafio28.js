const totalVoosDomesticos = db.voos.count({
  $and: [
    { "empresa.nome": "LATAM AIRLINES BRASIL" },
    { natureza: "Doméstica" },
  ],
});

db.resumoVoos.insertOne({ empresa: "LATAM AIRLINES BRASIL", totalVoosDomesticos });
db.resumoVoos.find({}, { _id: 0 });
