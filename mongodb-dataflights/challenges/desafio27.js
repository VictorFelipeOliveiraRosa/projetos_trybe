const totalVoosDomesticos = db.voos.count({
  $and: [
    { "empresa.nome": "PASSAREDO" },
    { natureza: "Doméstica" },
  ],
});

db.resumoVoos.insertOne({ empresa: "PASSAREDO", totalVoosDomesticos });
db.resumoVoos.find({}, { _id: 0 });
